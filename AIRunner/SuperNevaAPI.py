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
    DeviceList,
    DeviceListFilterInput,
    DeviceListSortInput,
    File,
    Info,
    Interest,
    InterestInput,
    InterestList,
    InterestListFilterInput,
    InterestListSortInput,
    Locale,
    LocationList,
    LocationListFilterInput,
    LocationListSortInput,
    LogInput,
    LogList,
    LogListFilterInput,
    LogListSortInput,
    Meta,
    MetaList,
    MetaListFilterInput,
    MetaListSortInput,
    Prompt,
    PromptInput,
    PromptList,
    PromptListFilterInput,
    PromptListSortInput,
    ReactionList,
    ReactionListFilterInput,
    ReactionListSortInput,
    ServiceInput,
    Session,
    SimpleResponse,
    StateList,
    StateListFilterInput,
    StateListSortInput,
    Target,
    TargetList,
    TargetListFilterInput,
    TargetListSortInput
)

class Prompts(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def get(self, promptId: "str", _auth: Optional[Auth] = None) -> Prompt:
        return self.request("/prompts/:promptId", body={"promptId": promptId}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["PromptListSortInput"]], filters: Optional["PromptListFilterInput"], _auth: Optional[Auth] = None) -> PromptList:
        return self.request("/prompts", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

    def run(self, _auth: Optional[Auth] = None) -> Any:
        return self.request("/prompts/run", body={}, _auth)  # type: ignore


class Targets(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["TargetListSortInput"]], filters: Optional["TargetListFilterInput"], _auth: Optional[Auth] = None) -> TargetList:
        return self.request("/targets", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

    def get(self, targetId: "str", _auth: Optional[Auth] = None) -> Target:
        return self.request("/targets/:targetId", body={"targetId": targetId}, _auth)  # type: ignore


class Reactions(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ReactionListSortInput"]], filters: Optional["ReactionListFilterInput"], _auth: Optional[Auth] = None) -> ReactionList:
        return self.request("/reactions", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Metas(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def get(self, metaId: "str", _auth: Optional[Auth] = None) -> Meta:
        return self.request("/metas/:metaId", body={"metaId": metaId}, _auth)  # type: ignore

    def create(self, data: List["None"], _auth: Optional[Auth] = None) -> MetaList:
        return self.request("metas/create", body={"data": data}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["MetaListSortInput"]], filters: Optional["MetaListFilterInput"], _auth: Optional[Auth] = None) -> MetaList:
        return self.request("/metas", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Logs(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def create(self, data: Optional[List["LogInput"]], _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request("/logs/create", body={"data": data}, _auth)  # type: ignore


class Interests(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def create(self, data: "InterestInput", cleanCache: Optional["bool"], _auth: Optional[Auth] = None) -> Interest:
        return self.request("/interests/create", body={"data": data, "cleanCache": cleanCache}, _auth)  # type: ignore


class Info(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def list(self, locale: Optional["Locale"], clientType: Optional["str"], clientVersion: Optional["str"], _auth: Optional[Auth] = None) -> Info:
        return self.request("/info", body={"locale": locale, "clientType": clientType, "clientVersion": clientVersion}, _auth)  # type: ignore


class Files(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def upload(self, data: "str", contentType: "str", filename: Optional["str"], path: Optional["str"], key: Optional["str"], _auth: Optional[Auth] = None) -> File:
        return self.request("/files/upload", body={"data": data, "contentType": contentType, "filename": filename, "path": path, "key": key}, _auth)  # type: ignore


class Contents(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def get(self, contentId: Optional["str"], key: Optional["str"], _auth: Optional[Auth] = None) -> Content:
        return self.request("/contents/:contentId", body={"contentId": contentId, "key": key}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ContentListSortInput"]], filters: Optional["ContentListFilterInput"], _auth: Optional[Auth] = None) -> ContentList:
        return self.request("/contents", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Collections(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def get(self, collectionId: "str", _auth: Optional[Auth] = None) -> Collection:
        return self.request("/collections/:collectionId", body={"collectionId": collectionId}, _auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["CollectionListSortInput"]], filters: Optional["CollectionListFilterInput"], _auth: Optional[Auth] = None) -> CollectionList:
        return self.request("/collections", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


class Auth(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def register_targets(self, _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request("/auth/register-targets", body={}, _auth)  # type: ignore

    def is_service_connected(self, _auth: Optional[Auth] = None) -> Any:
        return self.request("/auth/is-service-connected", body={}, _auth)  # type: ignore

    def login_with_token(self, token: "str", _auth: Optional[Auth] = None) -> Session:
        return self.request("/auth/login-with-token", body={"token": token}, _auth)  # type: ignore

    def connect_with_service(self, data: Optional["Any"], service: "ServiceInput", targetId: Optional["str"], targetKey: Optional["str"], _auth: Optional[Auth] = None) -> Session:
        return self.request("/auth/connect-with-service", body={"data": data, "service": service, "targetId": targetId, "targetKey": targetKey}, _auth)  # type: ignore

    def create_account(self, email: "str", password: "str", profile: Optional["AccountProfileInput"], settings: Optional["AccountSettingsInput"], targetId: Optional["str"], targetKey: Optional["str"], _auth: Optional[Auth] = None) -> Session:
        return self.request("/auth/create-account", body={"email": email, "password": password, "profile": profile, "settings": settings, "targetId": targetId, "targetKey": targetKey}, _auth)  # type: ignore


class Accounts(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    def me(self, _auth: Optional[Auth] = None) -> Any:
        return self.request("/accounts/me", body={}, _auth)  # type: ignore

    class me(SNRequest):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            super().__init__(*args, **kwargs)
        class collection(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["CollectionListSortInput"]], filters: Optional["CollectionListFilterInput"], _auth: Optional[Auth] = None) -> CollectionList:
                return self.request("/accounts/me/collections", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def create(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/collections/create", body={}, _auth)  # type: ignore

            def delete(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/collections/delete", body={}, _auth)  # type: ignore

            def update(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/collections/update", body={}, _auth)  # type: ignore

            def remove_content_from_collection(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/collections/remove-content-from-collection", body={}, _auth)  # type: ignore

            def add_content_to_collection(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/collections/add-content-to-collection", body={}, _auth)  # type: ignore


        class content(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ContentListSortInput"]], filters: Optional["ContentListFilterInput"], _auth: Optional[Auth] = None) -> ContentList:
                return self.request("/accounts/me/contents", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def create(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/contents/create", body={}, _auth)  # type: ignore

            def delete(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/contents/delete", body={}, _auth)  # type: ignore

            def update(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/contents/update", body={}, _auth)  # type: ignore

            def get(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/contents/:contentId", body={}, _auth)  # type: ignore


        class device(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["DeviceListSortInput"]], filters: Optional["DeviceListFilterInput"], _auth: Optional[Auth] = None) -> DeviceList:
                return self.request("/accounts/me/devices", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def save(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/devices/save", body={}, _auth)  # type: ignore

            def update(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/devices/update", body={}, _auth)  # type: ignore

            def delete(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/devices/delete", body={}, _auth)  # type: ignore

            def get(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/devices/:deviceId", body={}, _auth)


        class interest(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["InterestListSortInput"]], filters: Optional["InterestListFilterInput"], _auth: Optional[Auth] = None) -> InterestList:
                return self.request("/accounts/me/interests", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def get(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/interests/:interestId", body={}, _auth)  # type: ignore

            def create(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/interests/create", body={}, _auth)  # type: ignore

            def delete(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/interests/delete", body={}, _auth)  # type: ignore


        class location(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["LocationListSortInput"]], filters: Optional["LocationListFilterInput"], _auth: Optional[Auth] = None) -> LocationList:
                return self.request("/accounts/me/locations", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def register(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/locations/register", body={}, _auth)  # type: ignore

            def delete_all(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/locations/delete-all", body={}, _auth)  # type: ignore

            def create(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/locations/create", body={}, _auth)  # type: ignore


        class log(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["LogListSortInput"]], filters: Optional["LogListFilterInput"], _auth: Optional[Auth] = None) -> LogList:
                return self.request("/accounts/me/logs", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore


        class prompt(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["PromptListSortInput"]], filters: Optional["PromptListFilterInput"], _auth: Optional[Auth] = None) -> PromptList:
                return self.request("/accounts/me/prompts", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def get(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/prompts/:promptId", body={}, _auth)  # type: ignore

            def create(self, data: "PromptInput", _auth: Optional[Auth] = None) -> Prompt:
                return self.request("/accounts/me/prompts/create", body={"data": data}, _auth)  # type: ignore

            def update(self, promptId: "str", data: "PromptInput", _auth: Optional[Auth] = None) -> Prompt:
                return self.request("/accounts/me/prompts/update", body={"promptId": promptId, "data": data}, _auth)  # type: ignore

            def delete(self, promptId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
                return self.request("/accounts/me/prompts/delete", body={"promptId": promptId}, _auth)  # type: ignore


        class reaction(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def save(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/reactions/save", body={}, _auth)  # type: ignore


        class state(SNRequest):
            def __init__(self, *args: Any, **kwargs: Any) -> None:
                super().__init__(*args, **kwargs)
            def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["StateListSortInput"]], filters: Optional["StateListFilterInput"], _auth: Optional[Auth] = None) -> StateList:
                return self.request("/accounts/me/states", body={"_id": _id, "limit": limit, "skip": skip, "sort": sort, "filters": filters}, _auth)  # type: ignore

            def get(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/states/:stateId", body={}, _auth)  # type: ignore

            def save(self, _auth: Optional[Auth] = None) -> Any:
                return self.request("/accounts/me/states/save", body={}, _auth)  # type: ignore



