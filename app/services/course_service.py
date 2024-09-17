from typing import List, Optional
from ..models.course_model import Course, InitialCourse, CoverCourse, CourseWithInstructor
from ..services.instructor_service import InstructorService
from ..services.song_service import SongService

class CourseService:
    def __init__(self):
        self.instructor_service = InstructorService()
        self.song_service = SongService()
        
        instructors = self.instructor_service.get_all_instructors()
        if len(instructors) < 3:
            raise ValueError("Not enough instructors in the system")

        self.courses: List[Course] = [
            InitialCourse(
                id=1,
                title="Introduction à la guitare acoustique",
                description="Apprenez les bases de la guitare acoustique",
                instructor_id=instructors[1].id,
                duration=120,
                price=29.99,
                category='initial',
                video_url="/assets/video/lessons/armando_da_silva/caterine_ringer_cest_comme_ca/teazer/test_fr.mp4",
                star_rating=4,
                language="fr",
                instrument_id=1,
                concept="Accords de base et styles d'accompagnement"
            ),
            InitialCourse(
                id=2,
                title="Débutez au piano",
                description="Commencez votre voyage avec le piano",
                instructor_id=instructors[3].id,
                duration=90,
                price=19.99,
                category='initial',
                video_url="/assets/video/lessons/armando_da_silva/caterine_ringer_cest_comme_ca/teazer/test_fr.mp4",
                star_rating=5,
                language="fr",
                instrument_id=5,
                concept="Gammes de base (Majeur et Mineur)"
            ),
            CoverCourse(
                id=3,
                title="C'est comme ça, rithmique de base",
                description="Apprenez à jouer la partie rithmique de ce tube",
                instructor_id=instructors[0].id,
                duration=20,
                price=3.99,
                category='cover',
                video_url="/assets/video/lessons/armando_da_silva/caterine_ringer_cest_comme_ca/teazer/test_fr.mp4",
                star_rating=5,
                language="fr",
                instrument_id=1,
                song_id=2
            ),
            CoverCourse(
                id=4,
                title="Highway Star,",
                description="Get your amps ready friends !.",
                instructor_id=instructors[0].id,
                duration=45,
                price=4.99,
                category='cover',
                video_url="/assets/video/lessons/armando_da_silva/deep_purple_highway_star/teazer/test_en.mp4",
                star_rating=5,
                language="en",
                instrument_id=2,
                song_id=6
            ),
        ]

    def get_all_courses(self, language: Optional[str] = None) -> List[CourseWithInstructor]:
        courses = self.courses
        if language:
            courses = [course for course in courses if course.language == language]
        return [
            CourseWithInstructor(
                course=course,
                instructor=self.instructor_service.get_instructor_by_id(course.instructor_id)
            )
            for course in courses
        ]

    def get_initial_courses(self) -> List[CourseWithInstructor]:
        return [
            CourseWithInstructor(
                course=course,
                instructor=self.instructor_service.get_instructor_by_id(course.instructor_id)
            )
            for course in self.courses if isinstance(course, InitialCourse)
        ]

    def get_cover_courses(self) -> List[CourseWithInstructor]:
        return [
            CourseWithInstructor(
                course=course,
                instructor=self.instructor_service.get_instructor_by_id(course.instructor_id)
            )
            for course in self.courses if isinstance(course, CoverCourse)
        ]

    def get_course_by_id(self, course_id: int) -> Optional[CourseWithInstructor]:
        course = next((course for course in self.courses if course.id == course_id), None)
        if course:
            return CourseWithInstructor(
                course=course,
                instructor=self.instructor_service.get_instructor_by_id(course.instructor_id)
            )
        return None

    def get_courses_by_song_id(self, song_id: int) -> List[CourseWithInstructor]:
        return [
            CourseWithInstructor(
                course=course,
                instructor=self.instructor_service.get_instructor_by_id(course.instructor_id)
            )
            for course in self.courses
            if isinstance(course, CoverCourse) and course.song_id == song_id
        ]
