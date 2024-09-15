from pydantic import BaseModel
from typing import List

class InstructorBase(BaseModel):
    id: int
    name: str
    bio: str
    specialties: List[str]
    profile_picture_url: str
    rating: float
    instrument_ids: List[int]

class InstructorCreate(InstructorBase):
    pass

class Instructor(InstructorBase):
    class Config:
        orm_mode = True