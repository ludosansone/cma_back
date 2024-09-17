from typing import List, Optional
from datetime import datetime
from ..models.chapter_model import Chapter, ChapterCreate, ChapterUpdate, ChapterStatus

class ChapterService:
    def __init__(self):
        self.chapters: List[Chapter] = self.init_mock_chapters()

    def init_mock_chapters(self) -> List[Chapter]:
        mock_chapters = [
            Chapter(
                id=1,
                title="Introduction à la guitare acoustique",
                content="Dans ce chapitre, nous aborderons les bases de la guitare acoustique...",
                order=1,
                course_id=1,
                video_url="/assets/video/lessons/armando_da_silva/intro_acoustique/chapitre1.mp4",
                video_duration=600,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                status=ChapterStatus.PUBLISHED,
                tags=["débutant", "acoustique"],
                additional_resources=["https://example.com/ressources-supplementaires"]
            ),
            Chapter(
                id=2,
                title="Accords de base",
                content="Apprenons les accords fondamentaux pour jouer de la guitare acoustique...",
                order=2,
                course_id=1,
                video_url="/assets/video/lessons/armando_da_silva/intro_acoustique/chapitre2.mp4",
                video_duration=720,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                status=ChapterStatus.PUBLISHED,
                tags=["accords", "débutant"],
                additional_resources=[]
            ),
            Chapter(
                id=3,
                title="Introduction au piano",
                content="Découvrons les bases du piano et du clavier...",
                order=1,
                course_id=2,
                video_url="/assets/video/lessons/ludovic_sansone/intro_piano/chapitre1.mp4",
                video_duration=540,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                status=ChapterStatus.PUBLISHED,
                tags=["débutant", "piano"],
                additional_resources=["https://example.com/ressources-piano"]
            ),
            Chapter(
                id=4,
                title="Rythme de base pour 'C'est comme ça'",
                content="Apprenons le rythme de base de la chanson 'C'est comme ça'...",
                order=1,
                course_id=3,
                video_url="/assets/video/lessons/armando_da_silva/cest_comme_ca/chapitre1.mp4",
                video_duration=300,
                created_at=datetime.now(),
                updated_at=datetime.now(),
                status=ChapterStatus.PUBLISHED,
                tags=["rythme", "cover"],
                additional_resources=[]
            ),
        ]
        return mock_chapters

    def get_all_chapters(self) -> List[Chapter]:
        return self.chapters

    def get_chapter_by_id(self, chapter_id: int) -> Optional[Chapter]:
        return next((chapter for chapter in self.chapters if chapter.id == chapter_id), None)

    def create_chapter(self, chapter: ChapterCreate) -> Chapter:
        new_chapter = Chapter(
            id=len(self.chapters) + 1,
            **chapter.dict(),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.chapters.append(new_chapter)
        return new_chapter

    def update_chapter(self, chapter_id: int, chapter_update: ChapterUpdate) -> Optional[Chapter]:
        existing_chapter = self.get_chapter_by_id(chapter_id)
        if existing_chapter:
            update_data = chapter_update.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(existing_chapter, key, value)
            existing_chapter.updated_at = datetime.now()
            return existing_chapter
        return None

    def delete_chapter(self, chapter_id: int) -> bool:
        chapter = self.get_chapter_by_id(chapter_id)
        if chapter:
            self.chapters.remove(chapter)
            return True
        return False

    def get_chapters_by_course_id(self, course_id: int) -> List[Chapter]:
        return [chapter for chapter in self.chapters if chapter.course_id == course_id]
