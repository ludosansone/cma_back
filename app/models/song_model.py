from pydantic import BaseModel
from typing import Literal

class Song(BaseModel):
    id: int
    title: str
    artist: str
    originalReleaseYear: int
    tempo: int
    genre: str
    language: str
    version: Literal['live', 'studio']
    key: str
