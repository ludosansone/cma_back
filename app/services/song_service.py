from typing import List, Optional
from ..models.song_model import Song

class SongService:
    def __init__(self):
        self.songs: List[Song] = [
            Song(
                id=1,
                title="Je veux tout",
                artist="Ariane Noffatt",
                originalReleaseYear=2008,
                tempo=104,
                genre="Rock",
                language="fr",
                version="studio",
                key="Gm"
            ),
            Song(
                id=2,
                title="C'est comme ça",
                artist="Caterine Ringer",
                originalReleaseYear=1986,
                tempo=173,
                genre="Rock",
                language="fr",
                version="studio",
                key="F#"
            ),
            Song(
                id=3,
                title="Have You Ever Seen The Rain",
                artist="CCR",
                originalReleaseYear=1970,
                tempo=116,
                genre="Country",
                language="en",
                version="studio",
                key="Am"
            ),
            Song(
                id=4,
                title="Lookin' Out My Back Door",
                artist="CCR",
                originalReleaseYear=1970,
                tempo=103,
                genre="Country",
                language="en",
                version="studio",
                key="Bb"
            ),
            Song(
                id=5,
                title="Clocks",
                artist="Coldplay",
                originalReleaseYear=2002,
                tempo=133,
                genre="Pop",
                language="en",
                version="studio",
                key="Fm"
            ),
            Song(
                id=6,
                title="Highway Star",
                artist="Deep Purple",
                originalReleaseYear=1972,
                tempo=172,
                genre="Rock",
                language="en",
                version="studio",
                key="Gm"
            ),
            Song(
                id=7,
                title="Smoke On The Water",
                artist="Deep Purple",
                originalReleaseYear=1973,
                tempo=112,
                genre="Rock",
                language="en",
                version="studio",
                key="Gm"
            ),
            Song(
                id=8,
                title="Mes Blues passent pu dans porte",
                artist="Offenbach",
                originalReleaseYear=1979,
                tempo=105,
                genre="Pop",
                language="fr",
                version="studio",
                key="A"
            ),
            Song(
                id=9,
                title="The Logical Song",
                artist="Supertramp",
                originalReleaseYear=1979,
                tempo=116,
                genre="Pop",
                language="en",
                version="studio",
                key="Cm"
            ),
            Song(
                id=10,
                title="The Weight",
                artist="The Band",
                originalReleaseYear=1968,
                tempo=73,
                genre="Ballade",
                language="en",
                version="studio",
                key="A"
            ),
            Song(
                id=11,
                title="Je veux",
                artist="Aaz",
                originalReleaseYear=2010,
                tempo=156,
                genre="Pop",
                language="fr",
                version="studio",
                key="Dm"
            ),
        ]

    def get_all_songs(self) -> List[Song]:
        return self.songs

    def get_song_by_id(self, song_id: int) -> Optional[Song]:
        return next((song for song in self.songs if song.id == song_id), None)
