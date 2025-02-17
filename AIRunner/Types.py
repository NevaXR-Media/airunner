from enum import Enum
from typing import List, Optional, TypedDict, Dict, Any, Union, Literal
from datetime import date

from AIRunner.SuperNevaTypes import MLString, MLFile, File


class ContentStatus(str, Enum):
    FAILED = "failed"
    PROCESSING = "processing"
    READY = "ready"


class ContentFieldType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    BOOLEAN = "boolean"
    SELECTION = "selection"


class ContentBlockType(str, Enum):
    GENERIC = "generic"
    STACK = "stack"


class ContentBlockAppearance(str, Enum):
    GRID = "grid"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class ContentAction(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    label: Optional["MLString"]
    url: Optional[str]
    content: Optional[str]


class ContentNodeAsset(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    file: Optional["MLFile"]
    caption: Optional["MLString"]
    alt: Optional["MLString"]


class ContentNode(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional["MLString"]
    subtitle: Optional["MLString"]
    body: Optional["MLString"]
    date: Optional[date]
    assets: Optional[List[ContentNodeAsset]]
    resources: Optional[List[Dict[str, Optional[Union[str, "File"]]]]]
    actions: Optional[List[ContentAction]]
    meta: Optional[str]
    content: Optional[str]
    collection: Optional[str]
    prompt: Optional[str]
    sort: Optional[int]


class ContentLayout(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    appearance: Optional[ContentBlockAppearance]
    size: Optional[int]
    nodes: Optional[List[ContentNode]]


class ContentBlock(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional["MLString"]
    subtitle: Optional["MLString"]
    actions: Optional[List[ContentAction]]
    type: Optional[ContentBlockType]
    layout: Optional[ContentLayout]
    sort: Optional[int]


class ContentField(TypedDict, total=False):
    _id: Optional[str]
    label: Optional["MLString"]
    key: Optional[str]
    defaultValue: Optional[str]
    type: Optional[ContentFieldType]
    min: Optional[int]
    max: Optional[int]


class ContentAsset(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional["MLString"]
    description: Optional["MLString"]
    file: Optional["File"]
    tags: Optional[List[str]]
    version: Optional[str]
    maxVersion: Optional[str]
    minVersion: Optional[str]


class ContentSourceFilter(TypedDict, total=False):
    keyword: Optional[str]
    interested: Optional[bool]
    recently: Optional[bool]
    liked: Optional[bool]
    random: Optional[bool]
    tags: Optional[List[str]]
    targets: Optional[List[str]]


class ContentSourceSort(TypedDict, total=False):
    key: Optional[str]
    order: Optional[int]


class ContentQuery(TypedDict, total=False):
    filters: Optional[ContentSourceFilter]
    sort: Optional[List[ContentSourceSort]]


class ContentSource(TypedDict, total=False):
    _id: Optional[str]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional[str]
    key: Optional[str]
    contents: Optional[List[str]]
    query: Optional[ContentQuery]


class ContentVariant(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional[str]
    tags: Optional[List[str]]
    payload: Optional[Dict[str, Any]]
    assets: Optional[List["ContentAsset"]]
    sources: Optional[List["ContentSource"]]
    fields: Optional[List["ContentField"]]
    disabled: Optional[bool]
    highlighted: Optional[bool]
    createdAt: Optional[date]
    updatedAt: Optional[date]


class ContentCredit(TypedDict, total=False):
    _id: Optional[str]
    subject: Optional[str]
    role: Optional[str]
    primary: Optional[bool]


class Content(TypedDict, total=False):
    _id: Optional[str]
    status: Optional["ContentStatus"]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional[str]
    assets: Optional[List["ContentAsset"]]
    sources: Optional[List["ContentSource"]]
    variants: Optional[List["ContentVariant"]]
    fields: Optional[List["ContentField"]]
    promptId: Optional[str]
    callbackUrl: Optional[str]
    callbackTriggerAttempts: Optional[int]
    promptParams: Optional[Dict[str, Any]]
    promptResults: Optional[Dict[str, Any]]
    targets: Optional[List[str]]
    collections: Optional[List[str]]
    tags: Optional[List[str]]
    disabled: Optional[bool]
    publishedAt: Optional[date]
    publishedUntil: Optional[date]
    published: Optional[bool]
    createdBy: Optional[str]
    updatedBy: Optional[str]
    createdAt: Optional[date]
    updatedAt: Optional[date]
    version: Optional[int]
    isFeatured: Optional[bool]
    location: Optional[Dict[str, Any]]
    key: Optional[str]
    input: Optional["File"]
    body: Optional["MLString"]
    blocks: Optional[List[ContentBlock]]
    credits: Optional[List["ContentCredit"]]
    resources: Optional[List[Dict[str, Optional[Union[str, "File"]]]]]
    _keywords: Optional[str]
    generated: Optional[bool]
    disabledAt: Optional[date]


class PromptMessage(TypedDict, total=False):
    prompt: "Prompt"
    content: "Content"
    params: Optional[Dict[str, Any]]
    results: Optional[Dict[str, Any]]
    accountId: Optional[str]


class AIRunnerPipelineResult(TypedDict, total=False):
    type: Literal["success", "error"]
    message: Optional[str]
    body: Dict[str, Any]


class Resource(TypedDict, total=False):
    key: Optional[str]
    value: Optional[str]
    attachment: Optional[File]


class SQSConfig(TypedDict, total=False):
    url: Optional[str]
    secret: Optional[str]
    key: Optional[str]
    region: Optional[str]


class ContentInitialParams(TypedDict, total=False):
    published: Optional[bool]
    tags: Optional[List[str]]
    targets: Optional[List[str]]


class Prompt(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional["MLString"]
    description: Optional["MLString"]
    picture: Optional["MLFile"]
    color: Optional[str]
    prompt: Optional[str]
    negative_prompt: Optional[str]
    resources: Optional[List[Resource]]
    fn: Optional[str]
    sqs: Optional[SQSConfig]
    webhook_url: Optional[str]
    tags: Optional[List[str]]
    targets: Optional[List[str]]
    _keywords: Optional[str]
    collections: Optional[List[str]]
    version: Optional[float]
    publishedAt: Optional[date]
    publishedUntil: Optional[date]
    published: Optional[bool]
    highlighted: Optional[bool]
    contentInitialParams: Optional[ContentInitialParams]
    lastRunAt: Optional[date]
    disabled: Optional[bool]
    disabledAt: Optional[date]
    createdBy: Optional[str]
    updatedBy: Optional[str]
    createdAt: Optional[date]
    updatedAt: Optional[date]
