from typing import TypedDict
from AIRunner.AIRunnerSQSConfig import SQSConfig
from SuperNeva.SNConfig import SNConfig


class AIRunnerConfig(TypedDict):
    name: str
    sqs_config: SQSConfig
    superneva: SNConfig
