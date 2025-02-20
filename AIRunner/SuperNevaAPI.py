from enum import Enum  # type: ignore
from datetime import date  # type: ignore
from typing import TypedDict, Optional, Any, List  # type: ignore
from SuperNeva import SNRequest, Auth

from SuperNevaTypes import (
    Account,
    AccountProfileInput,
    AccountSettingsInput,
    Collection,
    CollectionInput,
    CollectionList,
    CollectionListFilterInput,
    CollectionListSortInput,
    Content,
    ContentInput,
    ContentList,
    ContentListFilterInput,
    ContentListSortInput,
    Device,
    DeviceInput,
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
    Location,
    LocationInput,
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
    Reaction,
    ReactionInput,
    ReactionList,
    ReactionListFilterInput,
    ReactionListSortInput,
    ServiceInput,
    Session,
    SimpleResponse,
    State,
    StateInput,
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
        return self.request(f"/prompts/{promptId}", body={}, _auth=_auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["PromptListSortInput"]], filters: Optional["PromptListFilterInput"], _auth: Optional[Auth] = None) -> PromptList:
        return self.request("/prompts", body={}, _auth=_auth)  # type: ignore

    def run(self, _auth: Optional[Auth] = None) -> Any:
        return self.request("/prompts/run", body={}, _auth=_auth)  # type: ignore


class Targets(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["TargetListSortInput"]], filters: Optional["TargetListFilterInput"], _auth: Optional[Auth] = None) -> TargetList:
        return self.request("/targets", body={}, _auth=_auth)  # type: ignore

    def get(self, targetId: "str", _auth: Optional[Auth] = None) -> Target:
        return self.request(f"/targets/{targetId}", body={}, _auth=_auth)  # type: ignore


class Reactions(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ReactionListSortInput"]], filters: Optional["ReactionListFilterInput"], _auth: Optional[Auth] = None) -> ReactionList:
        return self.request("/reactions", body={}, _auth=_auth)  # type: ignore


class Metas(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def get(self, metaId: "str", _auth: Optional[Auth] = None) -> Meta:
        return self.request(f"/metas/{metaId}", body={}, _auth=_auth)  # type: ignore

    def create(self, data: List["None"], _auth: Optional[Auth] = None) -> MetaList:
        return self.request("metas/create", body={}, _auth=_auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["MetaListSortInput"]], filters: Optional["MetaListFilterInput"], _auth: Optional[Auth] = None) -> MetaList:
        return self.request("/metas", body={}, _auth=_auth)  # type: ignore


class Logs(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def create(self, data: Optional[List["LogInput"]], _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request("/logs/create", body={}, _auth=_auth)  # type: ignore


class Interests(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def create(self, data: "InterestInput", cleanCache: Optional["bool"], _auth: Optional[Auth] = None) -> Interest:
        return self.request("/interests/create", body={}, _auth=_auth)  # type: ignore


class Info(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def get(self, locale: Optional["Locale"], clientType: Optional["str"], clientVersion: Optional["str"], _auth: Optional[Auth] = None) -> Info:
        return self.request("/info", body={}, _auth=_auth)  # type: ignore


class Files(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def upload(self, data: "str", contentType: "str", filename: Optional["str"], path: Optional["str"], key: Optional["str"], _auth: Optional[Auth] = None) -> File:
        return self.request("/files/upload", body={}, _auth=_auth)  # type: ignore


class Contents(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def get(self, contentId: Optional["str"], key: Optional["str"], _auth: Optional[Auth] = None) -> Content:
        return self.request(f"/contents/{contentId}", body={}, _auth=_auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ContentListSortInput"]], filters: Optional["ContentListFilterInput"], _auth: Optional[Auth] = None) -> ContentList:
        return self.request("/contents", body={}, _auth=_auth)  # type: ignore


class Collections(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def get(self, collectionId: "str", _auth: Optional[Auth] = None) -> Collection:
        return self.request(f"/collections/{collectionId}", body={}, _auth=_auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["CollectionListSortInput"]], filters: Optional["CollectionListFilterInput"], _auth: Optional[Auth] = None) -> CollectionList:
        return self.request("/collections", body={}, _auth=_auth)  # type: ignore


class Auth(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def registerTargets(self, _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request("/auth/register-targets", body={}, _auth=_auth)  # type: ignore

    def isServiceConnected(self, _auth: Optional[Auth] = None) -> Any:
        return self.request("/auth/is-service-connected", body={}, _auth=_auth)  # type: ignore

    def loginWithToken(self, token: "str", _auth: Optional[Auth] = None) -> Session:
        return self.request("/auth/login-with-token", body={}, _auth=_auth)  # type: ignore

    def connectWithService(self, data: Optional["Any"], service: "ServiceInput", targetId: Optional["str"], targetKey: Optional["str"], _auth: Optional[Auth] = None) -> Session:
        return self.request("/auth/connect-with-service", body={}, _auth=_auth)  # type: ignore

    def createAccount(self, email: "str", password: "str", profile: Optional["AccountProfileInput"], settings: Optional["AccountSettingsInput"], targetId: Optional["str"], targetKey: Optional["str"], _auth: Optional[Auth] = None) -> Session:
        return self.request("/auth/create-account", body={}, _auth=_auth)  # type: ignore


class Accounts(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.me = AccountsMe(*args, **kwargs)


class AccountsMe(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.collections = AccountsMeCollections(*args, **kwargs)
        self.contents = AccountsMeContents(*args, **kwargs)
        self.devices = AccountsMeDevices(*args, **kwargs)
        self.interests = AccountsMeInterests(*args, **kwargs)
        self.locations = AccountsMeLocations(*args, **kwargs)
        self.logs = AccountsMeLogs(*args, **kwargs)
        self.prompts = AccountsMePrompts(*args, **kwargs)
        self.reactions = AccountsMeReactions(*args, **kwargs)
        self.states = AccountsMeStates(*args, **kwargs)

    def get(self, _auth: Optional[Auth] = None) -> Account:
        return self.request("/accounts/me", body={}, _auth=_auth)  # type: ignore


class AccountsMeCollections(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def get(self, collectionId: "str", _auth: Optional[Auth] = None) -> Collection:
        return self.request(f"/accounts/me/collections/{collectionId}", body={}, _auth=_auth)  # type: ignore

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["CollectionListSortInput"]], filters: Optional["CollectionListFilterInput"], _auth: Optional[Auth] = None) -> CollectionList:
        return self.request("/accounts/me/collections", body={}, _auth=_auth)  # type: ignore

    def create(self, data: "CollectionInput", _auth: Optional[Auth] = None) -> Collection:
        return self.request("/accounts/me/collections/create", body={}, _auth=_auth)  # type: ignore

    def delete(self, collectionId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request(f"/accounts/me/collections/delete/{collectionId}", body={}, _auth=_auth)  # type: ignore

    def update(self, collectionId: "str", data: "CollectionInput", _auth: Optional[Auth] = None) -> Collection:
        return self.request("/accounts/me/collections/update", body={}, _auth=_auth)  # type: ignore

    def removeContentFromCollection(self, collectionId: "str", contentId: "str", _auth: Optional[Auth] = None) -> Collection:
        return self.request("/accounts/me/collections/remove-content-from-collection", body={}, _auth=_auth)  # type: ignore

    def addContentToCollection(self, collectionId: "str", contentId: "str", _auth: Optional[Auth] = None) -> Collection:
        return self.request("/api/v1/accounts/me/collections/add-content-to-collection", body={}, _auth=_auth)  # type: ignore


class AccountsMeContents(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["ContentListSortInput"]], filters: Optional["ContentListFilterInput"], _auth: Optional[Auth] = None) -> ContentList:
        return self.request("/accounts/me/contents", body={}, _auth=_auth)  # type: ignore

    def create(self, data: "ContentInput", _auth: Optional[Auth] = None) -> Content:
        return self.request("/accounts/me/contents/create", body={}, _auth=_auth)  # type: ignore

    def delete(self, contentId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request(f"/accounts/me/contents/delete/{contentId}", body={}, _auth=_auth)  # type: ignore

    def update(self, contentId: "str", data: "ContentInput", _auth: Optional[Auth] = None) -> Content:
        return self.request("/accounts/me/contents/update", body={}, _auth=_auth)  # type: ignore

    def get(self, contentId: "str", _auth: Optional[Auth] = None) -> Content:
        return self.request(f"/accounts/me/contents/{contentId}", body={}, _auth=_auth)  # type: ignore


class AccountsMeDevices(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["DeviceListSortInput"]], filters: Optional["DeviceListFilterInput"], _auth: Optional[Auth] = None) -> DeviceList:
        return self.request("/accounts/me/devices", body={}, _auth=_auth)  # type: ignore

    def save(self, data: "DeviceInput", _auth: Optional[Auth] = None) -> Device:
        return self.request("/accounts/me/devices/save", body={}, _auth=_auth)  # type: ignore

    def update(self, deviceId: "str", data: "DeviceInput", _auth: Optional[Auth] = None) -> Device:
        return self.request("/accounts/me/devices/update", body={}, _auth=_auth)  # type: ignore

    def delete(self, deviceId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request(f"/accounts/me/devices/delete/{deviceId}", body={}, _auth=_auth)  # type: ignore

    def get(self, deviceId: "str", _auth: Optional[Auth] = None) -> Device:
        return self.request(f"/accounts/me/devices/{deviceId}", body={}, _auth=_auth)  # type: ignore


class AccountsMeInterests(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["InterestListSortInput"]], filters: Optional["InterestListFilterInput"], _auth: Optional[Auth] = None) -> InterestList:
        return self.request("/accounts/me/interests", body={}, _auth=_auth)  # type: ignore

    def get(self, interestId: "str", _auth: Optional[Auth] = None) -> Interest:
        return self.request(f"/accounts/me/interests/{interestId}", body={}, _auth=_auth)  # type: ignore

    def create(self, data: "InterestInput", cleanCache: Optional["bool"], _auth: Optional[Auth] = None) -> Interest:
        return self.request("/accounts/me/interests/create", body={}, _auth=_auth)  # type: ignore

    def delete(self, interestId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request(f"/accounts/me/interests/delete/{interestId}", body={}, _auth=_auth)  # type: ignore


class AccountsMeLocations(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["LocationListSortInput"]], filters: Optional["LocationListFilterInput"], _auth: Optional[Auth] = None) -> LocationList:
        return self.request("/accounts/me/locations", body={}, _auth=_auth)  # type: ignore

    def register(self, data: "LocationInput", _auth: Optional[Auth] = None) -> Location:
        return self.request("/accounts/me/locations/register", body={}, _auth=_auth)  # type: ignore

    def deleteAll(self, deviceId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request("/accounts/me/locations/delete-all", body={}, _auth=_auth)  # type: ignore


class AccountsMeLogs(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["LogListSortInput"]], filters: Optional["LogListFilterInput"], _auth: Optional[Auth] = None) -> LogList:
        return self.request("/accounts/me/logs", body={}, _auth=_auth)  # type: ignore

    def create(self, data: Optional[List["LogInput"]], _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request("/accounts/me/logs/create", body={}, _auth=_auth)  # type: ignore


class AccountsMePrompts(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["PromptListSortInput"]], filters: Optional["PromptListFilterInput"], _auth: Optional[Auth] = None) -> PromptList:
        return self.request("/accounts/me/prompts", body={}, _auth=_auth)  # type: ignore

    def get(self, promptId: "str", _auth: Optional[Auth] = None) -> Prompt:
        return self.request(f"/accounts/me/prompts/{promptId}", body={}, _auth=_auth)  # type: ignore

    def create(self, data: "PromptInput", _auth: Optional[Auth] = None) -> Prompt:
        return self.request("/accounts/me/prompts/create", body={}, _auth=_auth)  # type: ignore

    def update(self, promptId: "str", data: "PromptInput", _auth: Optional[Auth] = None) -> Prompt:
        return self.request("/accounts/me/prompts/update", body={}, _auth=_auth)  # type: ignore

    def delete(self, promptId: "str", _auth: Optional[Auth] = None) -> SimpleResponse:
        return self.request(f"/accounts/me/prompts/delete/{promptId}", body={}, _auth=_auth)  # type: ignore


class AccountsMeReactions(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def save(self, data: "ReactionInput", skipNotification: Optional["bool"], _auth: Optional[Auth] = None) -> Reaction:
        return self.request("/accounts/me/reactions/save", body={}, _auth=_auth)  # type: ignore


class AccountsMeStates(SNRequest):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def list(self, _id: Optional["str"], limit: Optional["int"], skip: Optional["int"], sort: Optional[List["StateListSortInput"]], filters: Optional["StateListFilterInput"], _auth: Optional[Auth] = None) -> StateList:
        return self.request("/accounts/me/states", body={}, _auth=_auth)  # type: ignore

    def get(self, stateId: Optional["str"], _auth: Optional[Auth] = None) -> State:
        return self.request(f"/accounts/me/states/{stateId}", body={}, _auth=_auth)  # type: ignore

    def save(self, data: "StateInput", _auth: Optional[Auth] = None) -> State:
        return self.request("/accounts/me/states/save", body={}, _auth=_auth)  # type: ignore

