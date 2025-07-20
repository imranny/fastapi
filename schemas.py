from typing import Optional
from pydantic import BaseModel


class UsersAdd(BaseModel):
    name: str
    age: str
    sex: Optional[str] = None
    job: Optional[str] = None

class Users(UsersAdd):
    id: int

class UsersID(BaseModel):
    ok: bool = True
    user_id: int
