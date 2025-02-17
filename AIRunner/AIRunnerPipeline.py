# Type definitions
from typing import Any, Dict, Generic, Literal, Optional, TypeVar, TypedDict

from AIRunner.AIRunner import AIRunner
from AIRunner.Types.PromptMessage import PromptMessage

TStore = TypeVar("TStore")


class AIRunnerPipelineResult(TypedDict, total=False):
    type: Literal["success", "error"]
    message: Optional[str]
    body: Dict[str, Any]


class AIRunnerPipeline(Generic[TStore]):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def setup(self, runner: AIRunner[TStore]) -> None:
        self.logger = runner.logger
        self.logger.debug("Runner setup started.")

        self.store = runner.store
        self.context = runner.context

    def load(self) -> None:
        self.logger.debug("Loading pipeline.")

    def download(self) -> None:
        self.logger.debug("Downloading pipeline.")

    def run(
        self, payload: PromptMessage, previousResults: Dict[str, AIRunnerPipelineResult]
    ) -> AIRunnerPipelineResult:
        self.logger.info("Pipeline started.")
        return {"body": {"message": "Pipeline finished."}, "type": "success"}
