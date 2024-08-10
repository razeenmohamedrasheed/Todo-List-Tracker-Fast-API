from pydantic import BaseModel

class Addtodo(BaseModel):
    user_id:int
    todo_name:str

class UpdateTodo(BaseModel):
    task_id:int
    task_name:str