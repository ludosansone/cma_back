from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Literal
from datetime import datetime
from enum import Enum

class ChapterStatus(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

class BaseChapter(BaseModel):
    id: int
    title: str
    content: str
    order: int
    course_id: int
    video_url: str
    video_duration: int  # durée en secondes
    created_at: datetime
    updated_at: datetime
    status: ChapterStatus
    tags: List[str] = []
    additional_resources: List[str] = []

class ChapterCreate(BaseModel):
    title: str
    content: str
    order: int
    course_id: int
    video_url: str
    video_duration: int
    status: ChapterStatus = ChapterStatus.DRAFT
    tags: List[str] = []
    additional_resources: List[str] = []

class ChapterUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    order: Optional[int] = None
    video_url: Optional[str] = None
    video_duration: Optional[int] = None
    status: Optional[ChapterStatus] = None
    tags: Optional[List[str]] = None
    additional_resources: Optional[List[str]] = None

Chapter = BaseChapter
