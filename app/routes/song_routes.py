from fastapi import APIRouter, HTTPException
from typing import List
from ..models.song_model import Song
from ..models.course_model import CoverCourse
from ..services.song_service import SongService
from ..services.course_service import CourseService

router = APIRouter()
song_service = SongService()
course_service = CourseService()

@router.get("/song", response_model=List[Song])
async def get_all_songs():
    return song_service.get_all_songs()

@router.get("/song/{song_id}", response_model=Song)
async def get_song_by_id(song_id: int):
    song = song_service.get_song_by_id(song_id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@router.get("/song/{song_id}/courses", response_model=List[CoverCourse])
async def get_courses_by_song_id(song_id: int):
    courses = course_service.get_courses_by_song_id(song_id)
    if not courses:
        raise HTTPException(status_code=404, detail="No courses found for this song")
    return courses
