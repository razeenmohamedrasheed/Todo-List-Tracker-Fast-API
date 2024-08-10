from pydantic import BaseModel

class Addtodo(BaseModel):
    user_id:int
    todo_name:str

class UpdateTodo(BaseModel):
    user_id:int
    task_id:int