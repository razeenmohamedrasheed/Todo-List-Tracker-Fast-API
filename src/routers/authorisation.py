from fastapi import APIRouter
from src.models.authorisation import SignUp

router = APIRouter()


@router.post('/signup')
def userSignup(payload:SignUp):
    return payload