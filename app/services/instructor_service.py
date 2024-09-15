from typing import List, Optional
from ..models.instructor_model import Instructor

class InstructorService:
    def __init__(self):
        self.instructors: List[Instructor] = [
            Instructor(
                id=1,
                name="John Doe",
                bio="Experienced guitar instructor with 10 years of teaching.",
                specialties=["Rock", "Blues"],
                profile_picture_url="https://example.com/john_doe.jpg",
                rating=4.8,
                instrument_ids=[1, 2]  # acoustic and electric guitar
            ),
            Instructor(
                id=2,
                name="Jane Smith",
                bio="Professional pianist and composer.",
                specialties=["Classical", "Jazz"],
                profile_picture_url="https://example.com/jane_smith.jpg",
                rating=4.9,
                instrument_ids=[5]  # piano
            ),
            Instructor(
                id=3,
                name="Bob Johnson",
                bio="Multi-instrumentalist with a focus on rock and pop.",
                specialties=["Rock", "Pop", "Multi-instrument"],
                profile_picture_url="https://example.com/bob_johnson.jpg",
                rating=4.7,
                instrument_ids=[1, 2, 3, 4]  # guitar, bass, drums
            ),
        ]

    def get_all_instructors(self) -> List[Instructor]:
        return self.instructors

    def get_instructor_by_id(self, instructor_id: int) -> Optional[Instructor]:
        return next((instructor for instructor in self.instructors if instructor.id == instructor_id), None)
