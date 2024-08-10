from fastapi import APIRouter,status
from src.models.todos import Addtodo,UpdateTodo
from src.utilities.dbutils import DButils

router = APIRouter(
    tags=["TODO CRUD"]
    )


@router.post('/todo',status_code=status.HTTP_201_CREATED)
def addTodo(payload:Addtodo):
    db = DButils()
    columns = ['todoname','user_id']
    values =(
                payload.todo_name,
                payload.user_id,
        )
    db.insert_query('todos',columns,values)
    return{
                "message":"Successfully added"
        }

@router.get('/todo',status_code=status.HTTP_200_OK)
def getIndividualTask(user_id):
    db = DButils()
    query = f"""select * from todos where user_id = '{user_id}' """
    data  = db.execute_query(query,True)
    return{
                "message":"Success",
                "data":data
        }

@router.put('/todo/{user_id}',status_code=status.HTTP_200_OK)
def updateTask(user_id:int,payload:UpdateTodo):
    # return task_id
    db = DButils()
    query = f"""select * from todos where user_id = {user_id} """
    datas  = db.execute_query(query,True)
    if len(datas)==0:
        return status.HTTP_404_NOT_FOUND
    for data in datas:
        if data['todo_id'] == payload.task_id:
             if data['todoname'] is not None:
                 data['todoname'] = payload.task_name
                 query = f"""UPDATE todos SET todoname ='{payload.task_name}' WHERE todo_id = {payload.task_id} """   
                 db.updateQuery(query)
                 return{
                     "message":"successfully updated"
                 }

@router.delete('/todo/{user_id}/{task_id}',status_code=status.HTTP_200_OK)
def deleteTask(user_id:int,payload:UpdateTodo):
    # return task_id
    db = DButils()
    query = f"""select * from todos where user_id = {user_id} """
    datas  = db.execute_query(query,True)
    if len(datas)==0:
        return status.HTTP_404_NOT_FOUND
    for data in datas:
        print(data)
               