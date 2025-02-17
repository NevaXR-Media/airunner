from typing import Any, Generic, List, TypeVar, Optional
from AIRunner.AIRunnerConfig import AIRunnerConfig
from AIRunner.AIRunnerLogger import AIRunnerLogger
from AIRunner.Types.PromptMessage import PromptMessage

TStore = TypeVar("TStore")

class AIRunner(Generic[TStore]):
    def __init__(
        self,
        config: AIRunnerConfig,
        pipes: List[Any] = ...,
        logger: Optional[AIRunnerLogger] = ...,
    ) -> None: ...
    def generate(self, payload: PromptMessage) -> Any: ...
    def start_consumer(self) -> None: ...
    def load(self, startConsumer: bool = ...) -> None: ...
