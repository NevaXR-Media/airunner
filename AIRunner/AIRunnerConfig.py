from typing import TypedDict
from AIRunner.AIRunnerSQSConfig import SQSConfig


class AIRunnerConfig(TypedDict):
    name: str
    sqs_config: SQSConfig
