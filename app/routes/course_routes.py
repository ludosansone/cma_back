from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from ..models.course_model import Course, InitialCourse, CoverCourse, CourseWithInstructor
from ..services.course_service import CourseService

router = APIRouter()
course_service = CourseService()

@router.get("/course", response_model=List[CourseWithInstructor])
async def get_all_courses(language: Optional[str] = Query(None, enum=['fr', 'en'])):
    return course_service.get_all_courses(language)

@router.get("/course/initial", response_model=List[CourseWithInstructor])
async def get_initial_courses():
    return course_service.get_initial_courses()

@router.get("/course/cover", response_model=List[CourseWithInstructor])
async def get_cover_courses():
    return course_service.get_cover_courses()

@router.get("/course/{course_id}", response_model=CourseWithInstructor)
async def get_course_by_id(course_id: int):
    course = course_service.get_course_by_id(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
