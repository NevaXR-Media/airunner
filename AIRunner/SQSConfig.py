class SQSConfig:
    url: str
    key: str
    secret: str
    region: str = "eu-central-1"
    batch_size: int = 1
    polling_wait_time_ms: int = 5000

    def __init__(
        self, url: str, key: str, secret: str, region: str = "eu-central-1"
    ) -> None:
        self.url = url
        self.key = key
        self.secret = secret
        self.region = region
