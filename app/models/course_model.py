from pydantic import BaseModel
from typing import List, Literal
from .instructor_model import Instructor

class BaseCourse(BaseModel):
    id: int
    title: str
    description: str
    instructor_id: int
    duration: int
    price: float
    category: Literal['initial', 'cover']
    video_url: str
    star_rating: Literal[1, 2, 3, 4, 5]
    language: Literal['fr', 'en']
    instrument_id: int

class InitialCourse(BaseCourse):
    category: Literal['initial'] = 'initial'
    concept: str

class CoverCourse(BaseCourse):
    category: Literal['cover'] = 'cover'
    song_id: int

Course = InitialCourse | CoverCourse

class CourseWithInstructor(BaseModel):
    course: Course
    instructor: Instructor
