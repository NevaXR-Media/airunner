import os
import json
import timeit
from typing import Any, Callable, Dict, Generic, List, TypeVar, Optional
import boto3  # type: ignore
from aws_sqs_consumer import Consumer, Message  # type: ignore
from AIRunner.AIRunnerConfig import AIRunnerConfig
from AIRunner.AIRunnerLogger import AIRunnerLogger
from AIRunner.AIRunnerGenericStore import AIRunnerGenericStore
from AIRunner.Types import AIRunnerPipelineResult
from SuperNeva.SuperNeva import SuperNeva
from SuperNeva.SNRequest import Auth
from SuperNeva.Types import LogInput, LogPayloadInput, LogTopic, LogType
from AIRunner.Types import PromptMessage
from SuperNeva.SNSQS import SNSQSConfig

# import jwt
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64
import json


TStore = TypeVar("TStore")


class AIRunner(Generic[TStore]):
    pipes: List[Any]

    config: "AIRunnerConfig"
    # context: SuperNeva

    def __init__(
        self,
        config: "AIRunnerConfig",
        pipes: List[Any] = [],
        logger: Optional[AIRunnerLogger] = None,
        onErrorHandler: Optional[
            Callable[
                [str, float, PromptMessage, Any],
                None,
            ]
        ] = None,
        onSuccessHandler: Optional[
            Callable[[PromptMessage, PromptMessage], None]
        ] = None,
        onLogHandler: Optional[Callable[[str, float, PromptMessage, Any], None]] = None,
    ) -> None:
        self.config = config
        self.store = AIRunnerGenericStore[TStore]()
        self.pipes = pipes or []
        self.logger = logger or AIRunnerLogger(name="AIRunner", colorize=False)
        # context = SuperNeva(config=config["superneva"])
        self.sqs = boto3.client(  # type: ignore
            "sqs",
            region_name=config["sqs_config"]["region"],
            aws_access_key_id=config["sqs_config"]["key"],
            aws_secret_access_key=config["sqs_config"]["secret"],
        )
        self.logger.info("Runner initialized.")
        print(" ")
        self.onErrorHandler = onErrorHandler
        self.onSuccessHandler = onSuccessHandler
        self.onLogHandler = onLogHandler

    def onSuccess(
        self, context: SuperNeva, message: PromptMessage, body: PromptMessage
    ) -> None:
        self.logger.info("Run successfully finished.")
        prompt = message.get("prompt")
        content = message.get("content")
        collection = message.get("collection")
        meta = message.get("meta")
        media = message.get("media")

        deduplicationId = "default"
        if content:
            deduplicationId = content.get("_id")
        if collection:
            deduplicationId = collection.get("_id")
        if meta:
            deduplicationId = meta.get("_id")
        if media:
            deduplicationId = media.get("_id")

        if context.isResponseQueueReady:
            if prompt:
                prompt_id = prompt.get("_id", "default")
                context.queue.push(  # type: ignore
                    body=json.dumps(body),
                    groupId=str(prompt_id),
                    deduplicationId=str(deduplicationId),
                )

        if self.onSuccessHandler:
            self.onSuccessHandler(message, body)

    def onLog(
        self,
        context: SuperNeva,
        message: str,
        duration: float,
        payload: PromptMessage,
        result: Any,
    ) -> None:
        self.logger.info("New Log: " + message)

        prompt = payload.get("prompt")
        content = payload.get("content")
        collection = payload.get("collection")
        meta = payload.get("meta")
        media = payload.get("media")

        related: Dict[str, str] = {}
        if content:
            related["contentId"] = str(content.get("_id") or "?")
        if collection:
            related["collectionId"] = str(collection.get("_id") or "?")
        if meta:
            related["metaId"] = str(meta.get("_id") or "?")
        if media:
            related["mediaId"] = str(media.get("_id") or "?")

        if not prompt:
            self.logger.error("Invalid prompt.")
            return

        if context.isSuperNevaReady:
            if prompt:
                log_data: LogInput = LogInput(
                    description=message,
                    topic=LogTopic.PROMPT,
                    type=LogType.EVENT,
                    payload=LogPayloadInput(
                        _id=str(prompt.get("_id") or "?"),
                        related=related,
                        key="taskMessage",
                        value={
                            "result": result,
                            "payload": payload,
                        },
                        message=message,
                        code="200",
                        duration=duration,
                    ),
                )
                context.logs.create(data=[log_data])
            else:
                self.logger.error("Invalid message.")

        if self.onLogHandler:
            self.onLogHandler(message, duration, payload, result)

    def onError(
        self,
        context: SuperNeva,
        message: str,
        duration: float,
        payload: PromptMessage,
        result: Any,
    ) -> None:
        self.logger.info("New Error: " + message)

        if context.isSuperNevaReady:
            prompt = payload.get("prompt")
            content = payload.get("content")
            collection = payload.get("collection")
            meta = payload.get("meta")
            media = payload.get("media")
            account_id = payload.get("accountId")
            related: Dict[str, str] = {}
            if content:
                related["contentId"] = str(content.get("_id") or "?")
            if collection:
                related["collectionId"] = str(collection.get("_id") or "?")
            if meta:
                related["metaId"] = str(meta.get("_id") or "?")
            if media:
                related["mediaId"] = str(media.get("_id") or "?")
            if prompt:
                log_data = LogInput(
                    description=message,
                    topic=LogTopic.PROMPT,
                    type=LogType.ERROR,
                    payload=LogPayloadInput(
                        _id=str(prompt.get("_id") or "?"),
                        related=related,
                        key="taskMessage",
                        value={
                            "result": result,
                            "payload": payload,
                        },
                        message=message,
                        code="500",
                        duration=duration,
                    ),
                )

                context.logs.create(data=[log_data], _auth=Auth(account_id=account_id))
            else:
                self.logger.error("Invalid message.")

        if self.onErrorHandler:
            self.onErrorHandler(message, duration, payload, result)

    def generate(self, payload: PromptMessage, context: SuperNeva) -> Any:

        content = payload.get("content")
        collection = payload.get("collection")
        meta = payload.get("meta")
        media = payload.get("media")

        if content:
            self.onLog(
                context,
                "Generating prompt: " + str(content.get("_id")),
                0,
                payload,
                None,
            )
        if collection:
            self.onLog(
                context,
                "Generating collection: " + str(collection.get("_id")),
                0,
                payload,
                None,
            )
        if meta:
            self.onLog(
                context, "Generating meta: " + str(meta.get("_id")), 0, payload, None
            )
        if media:
            self.onLog(
                context, "Generating media: " + str(media.get("_id")), 0, payload, None
            )

        start_time = timeit.default_timer()
        if not self.pipes:
            self.logger.error("No pipes found.")
            return

        results: Dict[str, AIRunnerPipelineResult] = {}
        pipe_index = 0

        try:
            while pipe_index < len(self.pipes):
                pipe = self.pipes[pipe_index]
                is_last_pipe = pipe_index == len(self.pipes) - 1

                result = pipe.run(context, payload, results)

                print(result)
                if result.get("type") == "error":
                    duration = timeit.default_timer() - start_time
                    self.onError(
                        context,
                        "Error in pipe: " + pipe.name,
                        duration,
                        payload,
                        result,
                    )
                    return
                else:
                    if is_last_pipe:
                        end_time = timeit.default_timer()
                        body = result.get("body")
                        body["duration"] = end_time - start_time
                        self.logger.info(
                            "Pipe "
                            + pipe.name
                            + " completed in "
                            + str(end_time - start_time)
                            + " seconds."
                        )
                        self.onLog(
                            context,
                            "Pipe "
                            + pipe.name
                            + " completed in "
                            + str(end_time - start_time)
                            + " seconds.",
                            end_time - start_time,
                            payload,
                            result,
                        )

                        self.onSuccess(context, message=payload, body=body)
                    else:
                        duration = timeit.default_timer() - start_time
                        self.onLog(
                            context,
                            "Pipe " + pipe.name + " completed.",
                            duration,
                            payload,
                            result,
                        )

                results[pipe.name] = result
                pipe_index += 1
        except Exception as e:
            duration = timeit.default_timer() - start_time
            self.logger.error("Exception in pipe: " + self.pipes[pipe_index].name, e)
            self.onError(
                context,
                "Exception in pipe: " + self.pipes[pipe_index].name,
                duration,
                payload,
                e,
            )
            return

        final_result = results[self.pipes[-1].name]
        return final_result

    def handle_message(self, message: Message) -> None:
        # self.logger.info("Received message: " + message.Body)

        body = json.loads(message.Body)

        if not body:
            self.logger.error("Invalid message body.")
            return

        if not body.get("prompt"):
            self.logger.error("Invalid message prompt.")
            return

        signature = body.get("signature")
        if not signature:
            self.logger.error("Invalid message signature.")
            return

        sqs_message_secret = os.getenv("SQS_MESSAGE_SECRET", "")  # RESPONSE QUEUE TOKEN

        secret = sqs_message_secret.encode()
        message_encrypted = body.get("signature")

        # AES expects a 32-byte key (for AES-256)
        key = SHA256.new(secret).digest()

        # Decode ciphertext from Base64
        raw = base64.b64decode(message_encrypted)

        # Split IV and actual ciphertext
        iv = raw[:16]
        ciphertext = raw[16:]

        # Decrypt
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)

        # Remove padding (PKCS7)
        pad_len = decrypted[-1]
        plaintext = decrypted[:-pad_len].decode()

        # parse plaintext as json
        decoded_payload = json.loads(plaintext)

        # response_queue_token = params.get("responseQueueToken")

        # decoded_payload = jwt.decode(
        #     response_queue_token, sqs_message_secret, algorithms=["HS256"]
        # )

        sqs_config: SNSQSConfig = {
            "url": decoded_payload["sqsQueueUrl"],
            "key": decoded_payload["sqsKey"],
            "secret": decoded_payload["sqsSecret"],
            "region": decoded_payload["sqsRegion"],
        }
        body["_env"] = {
            "sqs_config": sqs_config,
            "base_url": decoded_payload["apiUrl"],
            "public": decoded_payload["public"],
            "secret": decoded_payload["secret"],
        }
        context = SuperNeva(config=body["_env"])

        # payload: Any = makeClass(body)
        self.generate(payload=body, context=context)

    def start_consumer(self) -> None:
        self.logger.info("Starting consumer.")

        consumer = Consumer(
            queue_url=self.config["sqs_config"]["url"],
            sqs_client=self.sqs,  # type: ignore
            region=self.config["sqs_config"]["region"],
            polling_wait_time_ms=self.config["sqs_config"]["polling_wait_time_ms"],
            batch_size=self.config["sqs_config"]["batch_size"],
        )

        if self.config["sqs_config"]["url"]:
            self.logger.info("Consumer started.")
            consumer.handle_message = self.handle_message
            consumer.start()  # type: ignore
        else:
            self.logger.error("Consumer not started. No SQS URL found.")

    def load(self, startConsumer: bool = True) -> None:
        for pipe in self.pipes:
            # Setup the pipe
            pipe.setup(runner=self)
            # Download the pipe required resources
            pipe.download()
            # Load the pipe
            pipe.load()
            print(" ")

        if startConsumer:
            self.start_consumer()
