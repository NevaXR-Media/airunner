from AIRunner.SQSConfig import SQSConfig
from SuperNeva.SuperNeva import SNConfig


class AIRunnerConfig:
    name: str
    sqs_config: SQSConfig
    superneva: SNConfig

    def __init__(
        self,
        name: str,
        sqs_config: SQSConfig,
        superneva: SNConfig,
    ) -> None:
        self.name = name
        self.sqs_config = sqs_config
        self.superneva = superneva
