from enum import Enum
from typing import List, Optional, TypedDict, Any, Literal, Dict
from datetime import datetime

#
#
# NCORE DB MODEL TYPES
#
#


class DisableReason(str, Enum):
    DELETED = "deleted"
    DISABLED = "disabled"
    DEACTIVATED = "deactivated"
    DISABLED_BY_PARENT = "disabled-by-parent"
    MERGED = "merged"
    NONE = "none"


class ContentBlockType(str, Enum):
    GENERIC = "generic"
    STACK = "stack"


class ContentBlockAppearance(str, Enum):
    GRID = "grid"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class ContentStatus(str, Enum):
    FAILED = "failed"
    PROCESSING = "processing"
    READY = "ready"


class ContentModerationStatus(str, Enum):
    CLEARED = "cleared"
    FLAGGED = "flagged"
    APPROVED = "approved"
    REJECTED = "rejected"


class ContentFieldType(str, Enum):
    TEXT = "text"
    NUMBER = "number"
    BOOLEAN = "boolean"
    SELECTION = "selection"


class FileMeta(TypedDict, total=False):
    name: Optional[str]
    size: Optional[int]
    duration: Optional[int]
    type: Optional[str]
    preview: Optional[bool]
    width: Optional[int]
    height: Optional[int]
    color: Optional[str]
    blurHash: Optional[str]


class StreamInfo(TypedDict, total=False):
    _id: Optional[str]
    url: Optional[str]
    thumbnails: Optional[List[str]]


class FileURLs(TypedDict, total=False):
    original: Optional[str]
    attribution: Optional[str]
    tracker: Optional[str]
    stream: Optional[StreamInfo]
    thumbnail: Optional[str]
    medium: Optional[str]
    large: Optional[str]
    xlarge: Optional[str]


class FileOwner(TypedDict, total=False):
    _id: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    picture: Optional[str]
    url: Optional[str]


class File(TypedDict, total=False):
    _id: Optional[str]
    urls: Optional[FileURLs]
    path: Optional[str]
    key: Optional[str]
    bucket: Optional[str]
    name: Optional[str]
    meta: Optional[FileMeta]
    origin: Optional[str]
    acl: Optional[str]
    createdBy: Optional[FileOwner]
    order: Optional[int]


class MLString(TypedDict, total=False):
    en: Optional[str]
    tr: Optional[str]
    es: Optional[str]
    de: Optional[str]
    fr: Optional[str]
    it: Optional[str]


class MLFile(TypedDict, total=False):
    en: Optional[File]
    tr: Optional[File]
    es: Optional[File]
    de: Optional[File]
    fr: Optional[File]
    it: Optional[File]


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


class ContentModerationCategory(TypedDict, total=False):
    flagged: Optional[bool]
    score: Optional[float]
    key: Optional[str]


class ContentAction(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    label: Optional[MLString]
    url: Optional[str]
    content: Optional[str]


class ContentNodeAsset(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    file: Optional[MLFile]
    caption: Optional[MLString]
    alt: Optional[MLString]


class ContentNode(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional[MLString]
    subtitle: Optional[MLString]
    body: Optional[MLString]
    date: Optional[datetime]
    assets: Optional[List[ContentNodeAsset]]
    resources: Optional[List[Resource]]
    actions: Optional[List[ContentAction]]
    url: Optional[str]
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
    sort: Optional[int]


class ContentBlock(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional[MLString]
    subtitle: Optional[MLString]
    actions: Optional[List[ContentAction]]
    type: Optional[ContentBlockType]
    appearance: Optional[ContentBlockAppearance]
    size: Optional[int]
    nodes: Optional[List[ContentNode]]
    sort: Optional[int]


class ContentAsset(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional[MLString]
    description: Optional[MLString]
    file: Optional[File]
    tags: Optional[List[str]]
    version: Optional[str]
    maxVersion: Optional[str]
    minVersion: Optional[str]


class ContentVariant(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional[MLString]
    description: Optional[MLString]
    picture: Optional[MLFile]
    color: Optional[str]
    tags: Optional[List[str]]
    payload: Optional[Dict[str, Any]]
    assets: Optional[List[ContentAsset]]
    disabled: Optional[bool]
    highlighted: Optional[bool]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]


class ContentCredit(TypedDict, total=False):
    _id: Optional[str]
    subject: Optional[str]
    role: Optional[str]
    primary: Optional[bool]


class Prompt(TypedDict, total=False):
    key: Optional[str]
    title: Optional[MLString]
    description: Optional[MLString]
    picture: Optional[MLFile]
    color: Optional[str]

    prompt: Optional[str]
    negativePrompt: Optional[str]
    resources: Optional[List[Resource]]

    fn: Optional[str]
    sqs: Optional[SQSConfig]
    webhookUrl: Optional[str]

    tags: Optional[List[str]]
    targetId: str
    keywords: Optional[str]

    collections: Optional[List[str]]
    version: Optional[int]

    publishedAt: Optional[datetime]
    publishedUntil: Optional[datetime]

    published: Optional[bool]
    highlighted: Optional[bool]

    contentInitialParams: Optional[ContentInitialParams]

    lastRunAt: Optional[datetime]

    disabled: Optional[bool]
    disableReason: Optional[DisableReason]
    disabledAt: Optional[datetime]

    createdBy: Optional[str]
    updatedBy: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]


class ContentModeration(TypedDict, total=False):
    status: Optional[ContentModerationStatus]
    report: Optional[List[ContentModerationCategory]]


class GeoLocation(TypedDict, total=False):
    type: Optional[str]
    coordinates: Optional[List[float]]


class Content(TypedDict, total=False):
    _id: Optional[str]
    key: Optional[str]
    title: Optional[MLString]
    description: Optional[MLString]
    picture: Optional[MLFile]
    color: Optional[str]
    locale: Optional[str]
    location: Optional[GeoLocation]

    status: Optional[ContentStatus]

    input: Optional[File]

    assets: Optional[List[ContentAsset]]
    variants: Optional[List[ContentVariant]]

    body: Optional[MLString]
    blocks: Optional[List[ContentBlock]]

    collections: Optional[List[str]]
    credits: Optional[List[ContentCredit]]
    resources: Optional[List[Resource]]

    targetId: str

    tags: Optional[List[str]]

    publishedAt: Optional[datetime]
    publishedUntil: Optional[datetime]
    published: Optional[bool]

    callbackUrl: Optional[str]
    callbackTriggerAttempts: Optional[int]

    promptId: Optional[str]
    promptParams: Optional[Dict[str, Any]]
    promptResults: Optional[Dict[str, Any]]
    promptGeneratedParams: Optional[Dict[str, Any]]

    moderation: Optional[ContentModeration]

    createdBy: Optional[str]
    updatedBy: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    disabled: Optional[bool]
    disabledAt: Optional[datetime]
    disableReason: Optional[DisableReason]


#
#
# AI RUNNER TYPES
#
#


class PromptMessage(TypedDict, total=False):
    # SQS Message fields
    _id: str
    prompt: Prompt
    content: Content
    params: Any
    results: Any
    accountId: str

    # AIRunner specific fields
    duration: Optional[float]
    message: Optional[str]


class AIRunnerPipelineResult(TypedDict, total=False):
    type: Literal["success", "error"]
    message: Optional[str]
    body: PromptMessage
