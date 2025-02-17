import json
import timeit
from typing import Any, Dict, Generic, List, TypeVar, Optional
import boto3  # type: ignore
from aws_sqs_consumer import Message  # type: ignore
from AIRunner.AIRunnerConfig import AIRunnerConfig
from AIRunner.AIRunnerLogger import AIRunnerLogger
from AIRunner.AIRunnerGenericStore import AIRunnerGenericStore
from AIRunner.SuperNeva.SuperNeva import SuperNeva
from AIRunner.Types.PromptMessage import PromptMessage


TStore = TypeVar("TStore")


class makeClass(object):
    def __init__(self, d: Any):
        for k, v in d.items():
            if isinstance(k, (list, tuple)):
                setattr(
                    self, k, [makeClass(x) if isinstance(x, dict) else x for x in v]  # type: ignore
                )
            else:
                setattr(self, k, makeClass(v) if isinstance(v, dict) else v)


class AIRunnerDebug(Generic[TStore]):
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
        self.sqs = None

        self.logger.info("Runner initialized.")
        print(" ")

    def onSuccess(self, message: PromptMessage, body: PromptMessage) -> None:
        self.logger.info("Run successfully finished.")

    def onLog(self, message: str, taskMessage: Any) -> None:
        self.logger.info("New Log: " + message)

    def onError(self, message: str, taskMessage: Any) -> None:
        self.logger.info("New Error: " + message)

    def generate(self, payload: PromptMessage) -> Any:

        content = payload.get("content")

        if not content:
            self.logger.error("Invalid content.")
            return

        self.onLog("Generating prompt: " + str(content.get("_id")), payload)
        start_time = timeit.default_timer()
        if not self.pipes:
            self.logger.error("No pipes found.")
            return

        results: Dict[str, Any] = {}
        pipe_index = 0

        try:
            while pipe_index < len(self.pipes):
                pipe = self.pipes[pipe_index]
                is_last_pipe = pipe_index == len(self.pipes) - 1

                if pipe_index > 0:
                    previous_pipe_result = results[self.pipes[pipe_index - 1].name]
                    payload["params"] = previous_pipe_result
                result: Any = pipe.run(payload, results)

                print(result)
                if result.get("type") == "error":
                    self.onError("Error in pipe: " + pipe.name, result)
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
                            result,
                        )

                        self.onSuccess(message=payload, body=body)
                    else:
                        self.onLog("Pipe " + pipe.name + " completed.", result)

                results[pipe.name] = result
                pipe_index += 1
        except Exception as e:
            self.logger.error("Exception in pipe: " + self.pipes[pipe_index].name, e)
            self.onError("Exception in pipe: " + self.pipes[pipe_index].name, e)
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

        if self.config.consumer_sqs_config.url:
            self.logger.info("Consumer started.")
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
