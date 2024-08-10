from pydantic import BaseModel

class SignUp(BaseModel):
    username:str
    email:str
    contact:str
    password:str