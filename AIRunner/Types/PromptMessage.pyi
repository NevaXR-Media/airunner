from typing import Any, Dict, Optional, TypedDict

from AIRunner.Types.Content import Content
from AIRunner.Types.Prompt import Prompt

class PromptMessage(TypedDict, total=False):
    prompt: Prompt
    content: Content
    params: Optional[Dict[str, Any]]
    results: Optional[Dict[str, Any]]
    accountId: Optional[str]
