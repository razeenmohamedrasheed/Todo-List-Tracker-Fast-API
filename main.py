from fastapi import FastAPI
from src.routers import authorisation,todos
import uvicorn


app = FastAPI(
    title="todoservices"
)

@app.get('/')
def welcome():
    return "Welcome"

app.include_router(authorisation.router)
app.include_router(todos.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)