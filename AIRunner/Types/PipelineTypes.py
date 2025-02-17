from typing import Any, Dict, Literal, Optional, TypedDict


class AIRunnerPipelineResult(TypedDict, total=False):
    type: Literal["success", "error"]
    message: Optional[str]
    body: Dict[str, Any]
