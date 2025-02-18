from SuperNevaTypes import Target
from SuperNevaTypes import TargetListFilterInput
from SuperNevaTypes import TargetListSortInput
from SuperNevaTypes import TargetList
from SuperNevaTypes import PromptListFilterInput
from SuperNevaTypes import PromptListSortInput
from SuperNevaTypes import PromptList
from SuperNevaTypes import Prompt
from enum import Enum
from datetime import date
from typing import TypedDict, Optional, Any, List

from SuperNeva import SNRequest, Auth

class Prompts(SNRequest):
    def get(self, promptId: "str", _auth: Optional[Auth] = None) -> Prompt:
        return self.request('/prompts/:promptId', body={"promptId": promptId}, _auth) # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["PromptListSortInput"]], filters: Optional["PromptListFilterInput"], _auth: Optional[Auth] = None) -> PromptList:
        return self.request('/prompts', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth) # type: ignore

class Targets(SNRequest):
    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["TargetListSortInput"]], filters: Optional["TargetListFilterInput"], _auth: Optional[Auth] = None) -> TargetList:
        return self.request('/targets', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth) # type: ignore

    def get(self, targetId: "str", _auth: Optional[Auth] = None) -> Target:
        return self.request('/targets/:targetId', body={"targetId": targetId}, _auth) # type: ignore
