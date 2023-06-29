from typing import List

import datetime

from autofastdantic.src.basemodel import BaseModel
from autofastdantic.src.utils.utc_datetime import utc_datetime


class Artist(BaseModel):
    class _Access:
        List=True
    name: str
    nationality: str
    location: str
    since: datetime.date
    biography: str


