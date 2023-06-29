from typing import List, Optional
from autofastdantic.src.basemodel import BaseModel


class Artwork(BaseModel):
    class _Access:
        List = True
    title: str
    year: int
    medium: str
    dimensions: str
    collection: str
    description: str
    image_urls: List[str]