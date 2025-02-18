from typing import Any, List, Optional
from typing_extensions import TypedDict
import requests
import boto3  # type: ignore
from AIRunner.AIRunnerConfig import AIRunnerConfig
from AIRunner.AIRunnerLogger import AIRunnerLogger
from AIRunner.SuperNevaTypes import File
from AIRunner.SuperNevaTypes import LogInput
from AIRunner.SuperNevaTypes import MetaInput


class Auth(TypedDict, total=False):
    account_id: Optional[str]
    token: Optional[str]
    provider: Optional[str]


class SNRequest:
    def __init__(self, config: AIRunnerConfig) -> None:
        self.config = config
        self.logger = AIRunnerLogger(name="SNRequest", colorize=False)
        self.base_url = config.base_url
        self.public = config.public

    def request(
        self,
        path: str,
        body: Any,
        auth: Optional[Auth] = None,
    ) -> Any:
        if auth is None:
            headers = {
                "content-type": "application/json",
                "x-public-key": self.public,
            }
        else:
            headers = {
                "content-type": "application/json",
                "x-public-key": self.public,
                "x-impersonate": (
                    auth.get("token")
                    if f"{auth.get('provider')}:::{auth.get('account_id')}:::{auth.get('token')}"
                    else f"{auth.get('provider')}:::{auth.get('account_id')}"
                ),
            }
        try:
            response = requests.post(self.base_url + path, headers=headers, json=body)
            return response.json()
        except Exception as e:
            self.logger.error("Request failed: " + path)
            return {
                "errors": [
                    {
                        "message": "Request failed",
                        "raw": str(e),
                    }
                ]
            }


class Logs(SNRequest):
    def create(self, data: LogInput) -> Any:
        data_array = [data]
        return self.request("/logs/create", {"data": data_array})


class Metas(SNRequest):
    def create(self, data: List[MetaInput], account_id: str) -> Any:
        return self.request(
            "/metas/create", {"data": data}, Auth(account_id=account_id)
        )

    def get(self, metaId: str, account_id: str) -> Any:
        return self.request(f"/metas/{metaId}", {}, Auth(account_id=account_id))


class Files(SNRequest):
    def upload(
        self,
        content_type: str,
        data: Any,
        account_id: str,
        path: Optional[str] = None,
        key: Optional[str] = None,
    ) -> Any:

        fileData = self.request(
            "/files/upload",
            {"key": key, "contentType": content_type, "data": data, "path": path},
            Auth(account_id=account_id),
        )
        # cast data["data"]["upload"] to File
        return File(**fileData)


class SNSQS:
    def __init__(self, config: AIRunnerConfig) -> None:
        self.config = config
        self.logger = AIRunnerLogger(name="SuperNeva", colorize=False)

        self.region_name = config.superneva_sqs_config.region
        self.aws_secret_access_key = config.superneva_sqs_config.secret
        self.aws_access_key_id = config.superneva_sqs_config.key
        self.url = config.superneva_sqs_config.url

        self.sqs = boto3.client(  # type: ignore
            "sqs",
            region_name=self.region_name,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )

        self.base_url = config.base_url
        self.public = config.public

    def push(self, body: Any, groupId: str, deduplicationId: str) -> None:
        self.logger.info("Pushing message to SQS")
        self.sqs.send_message(  # type: ignore
            QueueUrl=self.url,
            MessageBody=body,
            MessageGroupId=groupId,
            MessageDeduplicationId=deduplicationId,
        )


class SuperNeva:
    def __init__(self, config: AIRunnerConfig) -> None:
        self.config = config
        self.logger = AIRunnerLogger(name="SuperNeva", colorize=False)

        self.isSuperNevaReady = config.base_url != ""
        self.isConsumerReady = config.consumer_sqs_config.key != ""
        self.isResponseQueueReady = config.superneva_sqs_config.key != ""

        self.region_name = config.superneva_sqs_config.region
        self.aws_secret_access_key = config.superneva_sqs_config.secret
        self.aws_access_key_id = config.superneva_sqs_config.key

        self.sqs = boto3.client(  # type: ignore
            "sqs",
            region_name=self.region_name,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )

        self.base_url = config.base_url
        self.public = config.public

        self.logs = Logs(config)
        # self.metas = Metas(config)
        self.files = Files(config)
        self.metas = Metas(config)
        self.queue = SNSQS(config)
