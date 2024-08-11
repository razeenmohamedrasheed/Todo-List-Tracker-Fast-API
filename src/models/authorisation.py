from pydantic import BaseModel
from typing import Optional

class SignUp(BaseModel):
    username:str
    email:str
    contact:str
    password:str

class Login(BaseModel):
    username:str
    password:str

class TokenData(BaseModel):
    username:Optional[str] = None
