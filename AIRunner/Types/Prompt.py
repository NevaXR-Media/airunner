from typing import TYPE_CHECKING, Optional, List, TypedDict
from datetime import datetime

if TYPE_CHECKING:
    from AIRunner.SuperNeva.Types import MLString, MLFile, File


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
    publishedAt: Optional[datetime]
    publishedUntil: Optional[datetime]
    published: Optional[bool]
    highlighted: Optional[bool]
    contentInitialParams: Optional[ContentInitialParams]
    lastRunAt: Optional[datetime]
    disabled: Optional[bool]
    disabledAt: Optional[datetime]
    createdBy: Optional[str]
    updatedBy: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
