from fastapi import APIRouter,status,HTTPException
from src.models.authorisation import SignUp,Login
from src.utilities.dbutils import DButils
from passlib.context import CryptContext

router = APIRouter(
        tags=["Authorisation"]
)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

@router.post('/signup',status_code=status.HTTP_201_CREATED)
def userSignup(payload:SignUp):
        
        db = DButils()
        columns = ['username','email','contact','password']
        hashed_password = pwd_context.hash(payload.password)
        values =(
                payload.username,
                payload.email,
                payload.contact,
                hashed_password,
        )
        db.insert_query('users',columns,values)
        return{
                "message":"Signup Success"
        }

@router.post('login')
def userLogin(payload:Login):
        return payload

