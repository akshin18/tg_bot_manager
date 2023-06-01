from pydantic import BaseModel
from typing import Union



class Bots(BaseModel):
    id: int
    token:str
    name: Union[str,None] = None
    subs:Union[int,None] = None
    class Config:
        orm_mode = True
        
class Users(BaseModel):
    id: int
    username:str
    bot: int
    class Config:
        orm_mode = True



    

class AddBotSchema(BaseModel):
    name:str
    token:str