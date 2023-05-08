from fastapi import FastAPI
from router import Create, Read, Update, Delete 

app = FastAPI()
app.include_router(Read.router)