from fastapi import APIRouter
from Connection import engine
from sqlalchemy import text
from enum import Enum
import json

router = APIRouter(
    prefix='/read',
    tags=['read']
)

class readBy(str, Enum):
    json = 'JSON'
    uvicorn = 'UVICORN'

# Read header
@router.get('/get_header')
def get_data_header(read: readBy):
    c_engine = engine.connect()
    flag = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
    column_data = flag.fetchone()
    column_name = flag.keys()
    column_header = {name:data for name,data in zip(column_name, column_data)}
    data_return = json.dumps(column_header, default=str)
    engine.dispose()
    if read == read.uvicorn:
        return column_header
    else:
        return data_return

@router.get('/get_detail')
def get_data_detail(read:readBy):
    c_engine = engine.connect()
    flag = c_engine.execute(text('exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362'))
    column_data = flag.fetchall()
    column_name = flag.keys()
    column_detail = []
    for row in column_data:
        column_detail.append({name:data for name,data in zip(column_name, row)})
    data_return = json.dumps(column_detail, default=str)
    engine.dispose()
    if read == read.uvicorn:
        return column_detail 
    else:
        return data_return

@router.get('/get_all')
def get_all_data(read: readBy):
    c_engine = engine.connect()
    flag = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
    column_data = flag.fetchone()
    column_name = flag.keys()
    column_header = {name:data for name,data in zip(column_name, column_data)}
    column_header['items'] = get_data_detail(read.uvicorn)
    data_return = json.dumps(column_header, default=str)
    engine.dispose()
    if read == read.uvicorn:
        return column_header
    else:
        return data_return