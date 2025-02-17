import json
import timeit
from typing import Any, Dict, Generic, List, TypeVar, Optional
import boto3  # type: ignore
from aws_sqs_consumer import Consumer, Message  # type: ignore
from AIRunner.AIRunnerConfig import AIRunnerConfig
from AIRunner.AIRunnerLogger import AIRunnerLogger
from AIRunner.AIRunnerGenericStore import AIRunnerGenericStore
from AIRunner.Types import AIRunnerPipelineResult
from AIRunner.SuperNeva import SuperNeva
from AIRunner.SuperNevaTypes import LogInput, LogPayloadInput, LogTopic, LogType
from AIRunner.Types import PromptMessage

TStore = TypeVar("TStore")


class AIRunner(Generic[TStore]):
    config: AIRunnerConfig
    pipes: List[Any]

    context: SuperNeva

    def __init__(
        self,
        config: AIRunnerConfig,
        pipes: List[Any] = [],
        logger: Optional[AIRunnerLogger] = None,
    ) -> None:
        self.config = config
        self.store = AIRunnerGenericStore[TStore]()
        self.pipes = pipes or []
        self.logger = logger or AIRunnerLogger(name="AIRunner", colorize=False)
        self.context = SuperNeva(config)
        print(self.context)
        self.sqs = boto3.client(  # type: ignore
            "sqs",
            region_name=config.consumer_sqs_config.region,
            aws_access_key_id=config.consumer_sqs_config.key,
            aws_secret_access_key=config.consumer_sqs_config.secret,
        )

        self.logger.info("Runner initialized.")
        print(" ")

    def onSuccess(self, message: PromptMessage, body: PromptMessage) -> None:
        self.logger.info("Run successfully finished.")
        prompt = message.get("prompt")
        content = message.get("content")
        if prompt and content:
            self.context.queue.push(  # type: ignore
                body=json.dumps(body),
                groupId=prompt.get("_id") or "default",
                deduplicationId=content.get("_id") or "default",
            )

    def onLog(
        self, message: str, duration: float, payload: PromptMessage, result: Any
    ) -> None:
        self.logger.info("New Log: " + message)

        prompt = payload.get("prompt")
        content = payload.get("content")

        if not prompt:
            self.logger.error("Invalid prompt.")
            return

        if not content:
            self.logger.error("Invalid content.")
            return

        if prompt and content:

            log_data: LogInput = LogInput(
                description=message,
                topic=LogTopic.PROMPT,
                type=LogType.EVENT,
                payload=LogPayloadInput(
                    _id=str(prompt.get("_id") or "?"),
                    related={
                        "contentId": str(content.get("_id") or "?"),
                    },
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
            self.context.logs.create(log_data)
        else:
            self.logger.error("Invalid message.")

    def onError(
        self, message: str, duration: float, payload: PromptMessage, result: Any
    ) -> None:
        self.logger.info("New Error: " + message)

        prompt = payload.get("prompt")
        content = payload.get("content")

        if prompt and content:
            log_data = LogInput(
                description=message,
                topic=LogTopic.PROMPT,
                type=LogType.ERROR,
                payload=LogPayloadInput(
                    _id=str(prompt.get("_id") or "?"),
                    related={
                        "contentId": str(content.get("_id") or "?"),
                    },
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
            self.context.logs.create(log_data)
        else:
            self.logger.error("Invalid message.")

    def generate(self, payload: PromptMessage) -> Any:

        content = payload.get("content")

        if not content:
            self.logger.error("Invalid content.")
            return

        self.onLog("Generating prompt: " + str(content.get("_id")), 0, payload, None)
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

                result = pipe.run(payload, results)

                print(result)
                if result.get("type") == "error":
                    duration = timeit.default_timer() - start_time
                    self.onError(
                        "Error in pipe: " + pipe.name, duration, payload, result
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
                            "Pipe "
                            + pipe.name
                            + " completed in "
                            + str(end_time - start_time)
                            + " seconds.",
                            end_time - start_time,
                            payload,
                            result,
                        )

                        self.onSuccess(message=payload, body=body)
                    else:
                        duration = timeit.default_timer() - start_time
                        self.onLog(
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

        if not body.get("content"):
            self.logger.error("Invalid message content.")
            return

        if not body.get("prompt"):
            self.logger.error("Invalid message prompt.")
            return

        # payload: Any = makeClass(body)
        self.generate(payload=body)

    def start_consumer(self) -> None:
        self.logger.info("Starting consumer.")

        consumer = Consumer(
            queue_url=self.config.consumer_sqs_config.url,
            sqs_client=self.sqs,  # type: ignore
            region=self.config.consumer_sqs_config.region,
            polling_wait_time_ms=self.config.consumer_sqs_config.polling_wait_time_ms,
            batch_size=self.config.consumer_sqs_config.batch_size,
        )

        if self.config.consumer_sqs_config.url:
            self.logger.info("Consumer started.")
            consumer.handle_message = self.handle_message
            consumer.start()  # type: ignore
        else:
            self.logger.error("Consumer not started. No SQS URL found.")

    def load(self, startConsumer: bool = True) -> None:
        for pipe in self.pipes:
            # Setup the pipe
            pipe.setup(runner=self)
            pipe.download()
            # Load the pipe
            pipe.load()
            print(" ")

        if startConsumer:
            self.start_consumer()
