from connection.Connection import engine
from schema import header_schema, detail_schema
from sqlalchemy.orm import Session  
from connection import read_function
from fastapi import APIRouter, Depends
from connection.Connection import get_db

#initiate router
router = APIRouter(
    prefix='/read',
    tags=['read']
)

@router.get('/get_sales_order/{id}', response_model = header_schema)
async def get_sales_order(id: int, db: Session = Depends(get_db)):
    return read_function.join_all(db, id)