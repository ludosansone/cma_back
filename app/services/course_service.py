from typing import List, Optional
from ..models.course_model import Course, InitialCourse, CoverCourse, CourseWithInstructor
from ..services.instructor_service import InstructorService
from ..services.song_service import SongService

class CourseService:
    def __init__(self):
        self.instructor_service = InstructorService()
        self.song_service = SongService()
        
        # Assurons-nous d'abord que nous avons des instructeurs valides
        instructors = self.instructor_service.get_all_instructors()
        if len(instructors) < 3:
            raise ValueError("Not enough instructors in the system")

        self.courses: List[Course] = [
            InitialCourse(
                id=1,
                title="Introduction to Acoustic Guitar",
                description="Learn the basics of acoustic guitar playing",
                instructor_id=instructors[0].id,
                duration=60,
                price=29.99,
                category='initial',
                video_url="https://example.com/intro-acoustic-guitar",
                star_rating=4,
                language="en",
                instrument_id=1,
                concept="Basic chords and strumming patterns"
            ),
            InitialCourse(
                id=2,
                title="Piano for Beginners",
                description="Start your journey with piano",
                instructor_id=instructors[1].id,
                duration=90,
                price=39.99,
                category='initial',
                video_url="https://example.com/piano-beginners",
                star_rating=5,
                language="en",
                instrument_id=5,
                concept="Reading sheet music and basic scales"
            ),
            CoverCourse(
                id=3,
                title="Wonderwall Cover",
                description="Learn to play Wonderwall by Oasis",
                instructor_id=instructors[0].id,
                duration=45,
                price=24.99,
                category='cover',
                video_url="https://example.com/wonderwall-cover",
                star_rating=4,
                language="en",
                instrument_id=1,
                song_id=1
            ),
            CoverCourse(
                id=4,
                title="Bohemian Rhapsody on Piano",
                description="Master the iconic Bohemian Rhapsody by Queen",
                instructor_id=instructors[1].id,
                duration=120,
                price=49.99,
                category='cover',
                video_url="https://example.com/bohemian-rhapsody-piano",
                star_rating=5,
                language="en",
                instrument_id=5,
                song_id=3
            ),
            CoverCourse(
                id=5,
                title="Hotel California Full Band Cover",
                description="Learn to play all parts of Hotel California",
                instructor_id=instructors[2].id,
                duration=150,
                price=54.99,
                category='cover',
                video_url="https://example.com/hotel-california-cover",
                star_rating=5,
                language="en",
                instrument_id=2,
                song_id=7
            )
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
