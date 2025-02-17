from AIRunner.SQSConfig import SQSConfig


class AIRunnerConfig:
    name: str
    public: str
    base_url: str
    consumer_sqs_config: SQSConfig
    superneva_sqs_config: SQSConfig

    def __init__(
        self,
        name: str,
        public: str,
        base_url: str,
        consumer_sqs_config: SQSConfig,
        superneva_sqs_config: SQSConfig,
    ) -> None:
        self.name = name
        self.public = public
        self.base_url = base_url
        self.consumer_sqs_config = consumer_sqs_config
        self.superneva_sqs_config = superneva_sqs_config
