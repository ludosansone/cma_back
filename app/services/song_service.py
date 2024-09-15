from typing import List, Optional
from ..models.song_model import Song

class SongService:
    def __init__(self):
        self.songs: List[Song] = [
            Song(
                id=1,
                title="Wonderwall",
                artist="Oasis",
                originalReleaseYear=1995,
                tempo=87,
                genre="Rock",
                language="english",
                version="studio",
                key="F#m"
            ),
            Song(
                id=2,
                title="Shape of You",
                artist="Ed Sheeran",
                originalReleaseYear=2017,
                tempo=96,
                genre="Pop",
                language="english",
                version="studio",
                key="C#m"
            ),
            Song(
                id=3,
                title="Bohemian Rhapsody",
                artist="Queen",
                originalReleaseYear=1975,
                tempo=72,
                genre="Rock",
                language="english",
                version="studio",
                key="Bb"
            ),
            Song(
                id=7,
                title="Hotel California",
                artist="Eagles",
                originalReleaseYear=1977,
                tempo=75,
                genre="Rock",
                language="english",
                version="studio",
                key="Bm"
            ),
        ]

    def get_all_songs(self) -> List[Song]:
        return self.songs

    def get_song_by_id(self, song_id: int) -> Optional[Song]:
        return next((song for song in self.songs if song.id == song_id), None)
