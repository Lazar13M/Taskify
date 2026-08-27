from pydantic import BaseModel
from datetime import datetime

#Pydantic modeli znaci mora class ne moze def onda su obicne fje
class TaskCreate(BaseModel):
    title:str
    description:str|None=None

class TaskUpdate(BaseModel):
    title:str|None=None
    description:str|None=None
    completed:bool|None=None

class TaskOut(BaseModel):
    id:int
    title:str
    description:str|None=None
    completed:bool
    created_at:datetime