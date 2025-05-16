# Type definitions
from typing import Dict, Generic, TypeVar

from SuperNeva.SuperNeva import SuperNeva

from AIRunner.AIRunner import AIRunner
from AIRunner.Types import PromptMessage
from AIRunner.Types import AIRunnerPipelineResult

TStore = TypeVar("TStore")


class AIRunnerPipeline(Generic[TStore]):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def setup(self, runner: AIRunner[TStore]) -> None:
        self.logger = runner.logger
        self.logger.debug("Runner setup started.")

        self.store = runner.store

    def load(self) -> None:
        self.logger.debug("Loading pipeline.")

    def download(self) -> None:
        self.logger.debug("Downloading pipeline.")

    def run(
        self,
        context: SuperNeva,
        payload: PromptMessage,
        previousResults: Dict[str, AIRunnerPipelineResult],
    ) -> AIRunnerPipelineResult:
        self.logger.info("Pipeline started.")
        return {"body": {"message": "Pipeline finished."}, "type": "success"}
