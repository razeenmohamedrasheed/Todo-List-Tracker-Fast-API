from fastapi import APIRouter,status
from src.models.todos import Addtodo,UpdateTodo
from src.utilities.dbutils import DButils

router = APIRouter(
    tags=["todo services"]
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

@router.put('/todo/{task_id}',status_code=status.HTTP_200_OK)
def updateTask(task_id:int):
    return task_id
    # db = DButils()
    # query = f"""select * from todos where user_id = '{user_id}' and todo_id={todo_id} """
    # data  = db.execute_query(query,True)
    # return{
    #             "message":"Success",
    #             "data":data
    #     }