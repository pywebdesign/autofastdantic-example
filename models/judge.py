from autofastdantic.src.basemodel import BaseModel


class Judge(BaseModel):
    name: str
    title: str
    bio: str
    competition_id: int