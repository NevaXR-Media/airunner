from typing import TypedDict


class SQSConfig(TypedDict):
    url: str
    key: str
    secret: str
    region: str
    batch_size: int
    polling_wait_time_ms: int
