from autofastdantic.src.basemodel import BaseModel


class Competition(BaseModel):
    name: str
    start_date: str
    end_date: str
    location: str
    uri: str