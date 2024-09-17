from fastapi import APIRouter, HTTPException
from typing import List
from ..models.chapter_model import Chapter, ChapterCreate, ChapterUpdate
from ..services.chapter_service import ChapterService

router = APIRouter()
chapter_service = ChapterService()

@router.get("/chapter", response_model=List[Chapter])
async def get_all_chapters():
    return chapter_service.get_all_chapters()

@router.get("/chapter/{chapter_id}", response_model=Chapter)
async def get_chapter_by_id(chapter_id: int):
    chapter = chapter_service.get_chapter_by_id(chapter_id)
    if chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return chapter

@router.post("/chapter", response_model=Chapter)
async def create_chapter(chapter: ChapterCreate):
    return chapter_service.create_chapter(chapter)

@router.put("/chapter/{chapter_id}", response_model=Chapter)
async def update_chapter(chapter_id: int, chapter_update: ChapterUpdate):
    updated_chapter = chapter_service.update_chapter(chapter_id, chapter_update)
    if updated_chapter is None:
        raise HTTPException(status_code=404, detail="Chapter not found")
    return updated_chapter

@router.delete("/chapter/{chapter_id}", response_model=bool)
async def delete_chapter(chapter_id: int):
    if not chapter_service.delete_chapter(chapter_id):
        raise HTTPException(status_code=404, detail="Chapter not found")
    return True

@router.get("/course/{course_id}/chapters", response_model=List[Chapter])
async def get_chapters_by_course_id(course_id: int):
    chapters = chapter_service.get_chapters_by_course_id(course_id)
    if not chapters:
        raise HTTPException(status_code=404, detail="No chapters found for this course")
    return chapters
