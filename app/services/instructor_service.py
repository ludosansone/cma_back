from typing import List, Optional
from ..models.instructor_model import Instructor

class InstructorService:
    def __init__(self):
        self.instructors: List[Instructor] = [
            Instructor(
                id=1,
                name="Armando DA SILVA",
                bio="Professeur de guitare avec 20 ans d'expérience",
                specialties=["Rock", "Metal"],
                profile_picture_url="https://example.com/john_doe.jpg",
                rating=4.4,
                instrument_ids=[2]  
            ),
            Instructor(
                id=2,
                name="Étienne Gravel",
                bio="Professeur de guitare avec  12 ans d'expérience",
                specialties=["Rock", "Pop", "Blues"],
                profile_picture_url="https://example.com/john_doe.jpg",
                rating=4.8,
                instrument_ids=[1, 2]  
            ),
            Instructor(
                id=3,
                name="Lee Julien",
                bio="Professeur de batterie et guitare",
                specialties=["Rock", "Pop", "Blues", "Country"],
                profile_picture_url="https://example.com/john_doe.jpg",
                rating=5,
                instrument_ids=[1, 2, 4]
            ),
            Instructor(
                id=4,
                name="Ludovic Sansone",
                bio="Professeur de piano",
                specialties=["Pop", "Jazz", "Classique"],
                profile_picture_url="https://example.com/john_doe.jpg",
                rating=4.9,
                instrument_ids=[5]
            )
        ]

    def get_all_instructors(self) -> List[Instructor]:
        return self.instructors

    def get_instructor_by_id(self, instructor_id: int) -> Optional[Instructor]:
        return next((instructor for instructor in self.instructors if instructor.id == instructor_id), None)
