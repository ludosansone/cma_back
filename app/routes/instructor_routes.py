from fastapi import APIRouter, HTTPException
from typing import List
from ..models.instructor_model import Instructor
from ..services.instructor_service import InstructorService

router = APIRouter()
instructor_service = InstructorService()

@router.get("/instructor", response_model=List[Instructor])
async def get_all_instructors():
    return instructor_service.get_all_instructors()

@router.get("/instructor/{instructor_id}", response_model=Instructor)
async def get_instructor_by_id(instructor_id: int):
    instructor = instructor_service.get_instructor_by_id(instructor_id)
    if instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor
