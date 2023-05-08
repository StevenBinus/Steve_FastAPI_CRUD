from fastapi import APIRouter
from Connection import engine
from sqlalchemy import text
import json

column_header = {}
column_detail = {}

router = APIRouter(
    prefix='/read',
    tags=['read']
)

# Read header
@router.get('/get_header')
def get_data_header():
    c_engine = engine.connect()
    flag = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
    column_data = flag.fetchone()
    column_name = flag.keys()
    column_header = {name:data for name,data in zip(column_name, column_data)}
    data_return = json.dumps(column_header, default=str)
    engine.dispose()
    return data_return 

@router.get('/get_detail')
def get_data_detail():
    c_engine = engine.connect()
    flag = c_engine.execute(text('exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362'))
    column_data = flag.fetchall()
    column_name = flag.keys()
    column_detail = []
    for row in column_data:
        column_detail.append({name:data for name,data in zip(column_name, row)})
    data_return = json.dumps(column_detail, default=str)
    return data_return 

@router.get('/get_all')
def get_all_data():
    c_engine = engine.connect()
    flag = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
    column_data = flag.fetchone()
    column_name = flag.keys()
    column_header = {name:data for name,data in zip(column_name, column_data)}
    flag = c_engine.execute(text('exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362'))
    column_data = flag.fetchall()
    column_name = flag.keys()
    column_detail = [{name:data for name,data in zip(column_name, row)} for row in column_data]
    engine.dispose()
    data_return = []
    for detail in column_detail:
        item = {"item": {}}
        item["item"].update(column_header)
        item["item"].update(detail)
        data_return.append(item)
    return json.dumps(data_return, default=str)

    # header_data = get_data_header()
    # detail_data = get_data_detail()
    # all_data = header_data + detail_data
    # return all_data