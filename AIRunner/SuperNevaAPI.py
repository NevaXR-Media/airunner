from enum import Enum # type: ignore
from datetime import date # type: ignore
from typing import TypedDict, Optional, Any, List # type: ignore
from SuperNeva import SNRequest, Auth
from SuperNevaTypes import (
    AccountProfileInput,
    AccountSettingsInput,
    Collection,
    CollectionList,
    CollectionListFilterInput,
    CollectionListSortInput,
    Content,
    ContentList,
    ContentListFilterInput,
    ContentListSortInput,
    File,
    Info,
    Interest,
    InterestInput,
    Locale,
    LogInput,
    Meta,
    MetaList,
    MetaListFilterInput,
    MetaListSortInput,
    Prompt,
    PromptList,
    PromptListFilterInput,
    PromptListSortInput,
    ReactionList,
    ReactionListFilterInput,
    ReactionListSortInput,
    ServiceInput,
    Session,
    SimpleResponse,
    Target,
    TargetList,
    TargetListFilterInput,
    TargetListSortInput
)

class Prompts(SNRequest):
    def get(self, promptId: "str", _auth: Optional[Auth] = None) -> Prompt:
        return self.request('/prompts/:promptId', body={"promptId": promptId}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["PromptListSortInput"]], filters: Optional["PromptListFilterInput"], _auth: Optional[Auth] = None) -> PromptList:
        return self.request('/prompts', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

    def run(self, _auth: Optional[Auth] = None) -> Any:
        return self.request('/prompts/run', body={}, _auth)  # type: ignore


class Targets(SNRequest):
    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["TargetListSortInput"]], filters: Optional["TargetListFilterInput"], _auth: Optional[Auth] = None) -> TargetList:
        return self.request('/targets', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

    def get(self, targetId: "str", _auth: Optional[Auth] = None) -> Target:
        return self.request('/targets/:targetId', body={"targetId": targetId}, _auth)  # type: ignore


class Reactions(SNRequest):
    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ReactionListSortInput"]], filters: Optional["ReactionListFilterInput"], _auth: Optional[Auth] = None) -> ReactionList:
        return self.request('/reactions', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Metas(SNRequest):
    def get(self, metaId: "str", _auth: Optional[Auth] = None) -> Meta:
        return self.request('/metas/:metaId', body={"metaId": metaId}, _auth)  # type: ignore

    def create(self, data: List["None"], _auth: Optional[Auth] = None) -> MetaList:
        return self.request('metas/create', body={"data": data}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["MetaListSortInput"]], filters: Optional["MetaListFilterInput"], _auth: Optional[Auth] = None) -> MetaList:
        return self.request('/metas', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Logs(SNRequest):
    def create(self, data: Optional[List["LogInput"]], _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request('/logs/create', body={"data": data}, _auth)  # type: ignore


class Interests(SNRequest):
    def create(self, data: "InterestInput", cleanCache: Optional["bool"], _auth: Optional[Auth] = None) -> Interest:
        return self.request('/interests/create', body={"data": data, "cleanCache": cleanCache}, _auth)  # type: ignore


class Info(SNRequest):
    def list(self, locale: Optional["Locale"], clientType: Optional["str"], clientVersion: Optional["str"], _auth: Optional[Auth] = None) -> Info:
        return self.request('/info', body={"locale": locale, "clientType": clientType, "clientVersion": clientVersion}, _auth)  # type: ignore


class Files(SNRequest):
    def upload(self, data: "str", contentType: "str", filename: Optional["str"], path: Optional["str"], key: Optional["str"], _auth: Optional[Auth] = None) -> File:
        return self.request('/files/upload', body={"data": data, "contentType": contentType, "filename": filename, "path": path, "key": key}, _auth)  # type: ignore


class Contents(SNRequest):
    def get(self, contentId: Optional["str"], key: Optional["str"], _auth: Optional[Auth] = None) -> Content:
        return self.request('/contents/:contentId', body={"contentId": contentId, "key": key}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ContentListSortInput"]], filters: Optional["ContentListFilterInput"], _auth: Optional[Auth] = None) -> ContentList:
        return self.request('/contents', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Collections(SNRequest):
    def get(self, collectionId: "str", _auth: Optional[Auth] = None) -> Collection:
        return self.request('/collections/:collectionId', body={"collectionId": collectionId}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["CollectionListSortInput"]], filters: Optional["CollectionListFilterInput"], _auth: Optional[Auth] = None) -> CollectionList:
        return self.request('/collections', body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Auth(SNRequest):
    def register_targets(self, _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request('/auth/register-targets', body={}, _auth)  # type: ignore

    def is_service_connected(self, _auth: Optional[Auth] = None) -> Any:
        return self.request('/auth/is-service-connected', body={}, _auth)  # type: ignore

    def login_with_token(self, token: "str", _auth: Optional[Auth] = None) -> Session:
        return self.request('/auth/login-with-token', body={"token": token}, _auth)  # type: ignore

    def connect_with_service(self, data: Optional["Any"], service: "ServiceInput", targetId: Optional["str"], targetKey: Optional["str"], _auth: Optional[Auth] = None) -> Session:
        return self.request('/auth/connect-with-service', body={"data": data, "service": service, "targetId": targetId, "targetKey": targetKey}, _auth)  # type: ignore

    def create_account(self, email: "str", password: "str", profile: Optional["AccountProfileInput"], settings: Optional["AccountSettingsInput"], targetId: Optional["str"], targetKey: Optional["str"], _auth: Optional[Auth] = None) -> Session:
        return self.request('/auth/create-account', body={"email": email, "password": password, "profile": profile, "settings": settings, "targetId": targetId, "targetKey": targetKey}, _auth)  # type: ignore


class Accounts(SNRequest):
    class endpoints(SNRequest):
        def list(self, _auth: Optional[Auth] = None) -> Any:
            return self.request('None', body={}, _auth)  # type: ignore


