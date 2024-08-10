from pydantic import BaseModel

class SignUp(BaseModel):
    username:str
    email:str
    contact:str
    password:str

class Login(BaseModel):
    username:str
    password:str
