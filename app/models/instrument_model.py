from pydantic import BaseModel

class Instrument(BaseModel):
    id: int
    nameKey: str
    category: str
    icon: str | None = None
