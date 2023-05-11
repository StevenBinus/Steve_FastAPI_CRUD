from fastapi import APIRouter
from sqlalchemy import text
from enum import Enum
import json
# internal library
from Connection import engine
from Base_model import header_model, detail_model

#initiate router
router = APIRouter(
    prefix='/read',
    tags=['read']
)

# getting all data 
@router.get('/get_all')
def get_header():
    c_engine = engine.connect()
    # Header data
    flag_header = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
    result = flag_header.fetchone()
    table_model = header_model( 
        SOSysNo = result[1],  
        SODocNo = result[2], 
        SODate = result[3], 
        SOStatus = result[4], 
        CustomerCode = result[5], 
        CustomerName = result[6], 
        CustomerAddress = result[7], 
        CustomerMobilePhoneNo = result[8], 
        TOP = result[9], 
        TotalAmount = result[10], 
        SalesEmployeeNo = result[11], 
        SalesemployeeName = result[12],
        Items = [],
    )

    # Detail Data
    flag_detail = c_engine.execute(text('exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362'))
    detail_result = flag_detail.fetchall()
    for data in detail_result: # looping to get all item data based on the sp
        table_detail = detail_model(
            ItemCode = data[0],
            ItemName = data[1],
            QtyDemand = data[2],
            ItemPrice = data[3],
            DiscPercent = data[4],
            DiscAmount = data[5],
            LineTotal = data[6],
            QtySupplied = data[7]
        ) 
        table_model.Items.append(table_detail)
    engine.dispose()
    return table_model


# class readBy(str, Enum):
#     json = 'JSON'
#     uvicorn = 'UVICORN'

# # Read header
# @router.get('/get_header')
# def get_data_header(read: readBy):
#     c_engine = engine.connect()
#     flag = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
#     column_data = flag.fetchone()
#     column_name = flag.keys()
#     column_header = {name:data for name,data in zip(column_name, column_data)}
#     data_return = json.dumps(column_header, default=str)
#     engine.dispose()
#     if read == read.uvicorn:
#         return column_header
#     else:
#         return data_return

# @router.get('/get_detail')
# def get_data_detail(read:readBy):
#     c_engine = engine.connect()
#     flag = c_engine.execute(text('exec uspg_atSalesOrder1_Select @Option=50,@So_Sys_No=3635362'))
#     column_data = flag.fetchall()
#     column_name = flag.keys()
#     column_detail = []
#     for row in column_data:
#         column_detail.append({name:data for name,data in zip(column_name, row)})
#     data_return = json.dumps(column_detail, default=str)
#     engine.dispose()
#     if read == read.uvicorn:
#         return column_detail 
#     else:
#         return data_return

# @router.get('/get_all')
# def get_all_data(read: readBy):
#     c_engine = engine.connect()
#     flag = c_engine.execute(text('exec uspg_atSalesOrder0_Select @Option=51,@Company_Code=3125098,@So_Sys_No=3635362'))
#     column_data = flag.fetchone()
#     column_name = flag.keys()
#     column_header = {name:data for name,data in zip(column_name, column_data)}
#     column_header['items'] = get_data_detail(read.uvicorn)
#     data_return = json.dumps(column_header, default=str)
#     engine.dispose()
#     if read == read.uvicorn:
#         return column_header
#     else:
#         return data_return