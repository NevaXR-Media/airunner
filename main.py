from typing import Dict
from AIRunner.AIRunnerPipeline import AIRunnerPipeline
from AIRunner.SQSConfig import SQSConfig
from AIRunner.AIRunner import AIRunner

from AIRunner.AIRunnerConfig import AIRunnerConfig
from AIRunner.AIRunnerLogger import AIRunnerLogger
from AIRunner.Types import AIRunnerPipelineResult, PromptMessage


class MyStore:
    pass


class TestPipeline(AIRunnerPipeline[MyStore]):
    def __init__(self, name: str):
        super().__init__(name)

    def run(
        self, payload: PromptMessage, previousResults: Dict[str, AIRunnerPipelineResult]
    ) -> AIRunnerPipelineResult:
        self.logger.info("Pipeline started.")
        return {"body": {"message": "Pipeline finished."}, "type": "success"}


def TestRunner():
    # Create custom logger
    logger = AIRunnerLogger(name="AIRunner:Test", colorize=True, level="DEBUG")

    # Setup config
    config = AIRunnerConfig(
        name="Test",
        public="?",
        base_url="http://localhost:3000/api/v1",
        consumer_sqs_config=SQSConfig(
            url="",
            key="",
            secret="",
            region="",
        ),
        superneva_sqs_config=SQSConfig(
            url="",
            key="",
            secret="",
            region="",
        ),
    )

    # Setup pipes
    pipes: list[TestPipeline] = [TestPipeline(name="Test")]

    # Init runner
    runner = AIRunner[MyStore](config=config, pipes=pipes, logger=logger)

    return runner


runner = TestRunner()
