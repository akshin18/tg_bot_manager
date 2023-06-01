from pydantic import BaseModel
from typing import Union



class Bots(BaseModel):
    id: int
    token:str
    class Config:
        orm_mode = True


    

