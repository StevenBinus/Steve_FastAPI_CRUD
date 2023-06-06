from fastapi import FastAPI
from router import Create, Read, Update, Delete, New_read

app = FastAPI()
app.include_router(New_read.router)