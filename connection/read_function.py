from sqlalchemy.orm import Session
from sqlalchemy import label, func
from fastapi import status
from connection.Connection import get_db
from schema import header_schema, detail_schema
from model import header_model, detail_model, customer_model, sales_employee_model, item_model

def get_header_data(db = Session, id = int):
    header_data = (
        db.query(
            header_model.SO_SYS_NO.label('SOSysNo'),
            header_model.SO_DOC_NO.label('SODocNo'),
            header_model.SO_DATE.label('SODate'),
            header_model.SO_STATUS.label('SOStatus'),
            header_model.CUST_CODE.label('CustomerCode'),
            customer_model.CUSTOMER_NAME.label('CustomerName'),
            func.concat(
                header_model.DLVR_ADDR, 
                ',', 
                header_model.DLVR_ADDR1, 
                ',', 
                header_model.DLVR_ADDR2
            ).label('CustomerAddress'),
            customer_model.CUST_MOBILE_PHONE.label('CustomerMobilePhoneNo'),
            header_model.TOP_CODE.label('TOP'),
            header_model.TOTAL.label('TotalAmount'),
            header_model.SALES_EMP_NO.label('SalesEmployeeNo'),
            sales_employee_model.EMPLOYEE_NAME.label('SalesEmployeeName')
            ).join(
                customer_model, 
                customer_model.CUSTOMER_CODE == header_model.CUST_CODE, 
                isouter = True
            ).join(
                sales_employee_model, 
                sales_employee_model.EMPLOYEE_NO == header_model.SALES_EMP_NO, 
                isouter = True
            ).filter(header_model.SO_SYS_NO == id
            ).first()
        )
    if header_data is not None:
        return header_data
    else:
        return None

def get_detail_data(db = Session, id = int):
    detail_data = (
        db.query(
                detail_model.ITEM_CODE.label('ItemCode'),
                item_model.ITEM_NAME.label('ItemName'),
                detail_model.QTY_DEMAND.label('QtyDemand'),
                detail_model.PRICE.label('ItemPrice'),
                detail_model.DISC_PERCENT.label('DiscPercent'),
                detail_model.DISC_AMOUNT.label('DiscAmount'),
                func.sum(
                    detail_model.QTY_DEMAND * (detail_model.PRICE - detail_model.DISC_REQ_AMOUNT)
                ).label('LineTotal'),
                detail_model.QTY_SUPPLY.label('QtySupplied')
            ).join(item_model, item_model.ITEM_CODE == detail_model.ITEM_CODE
            ).filter(detail_model.SO_SYS_NO == id
            ).group_by(
                detail_model.ITEM_CODE,
                item_model.ITEM_NAME,
                detail_model.QTY_DEMAND,
                detail_model.PRICE,
                detail_model.DISC_PERCENT,
                detail_model.DISC_AMOUNT,
                detail_model.QTY_SUPPLY
            ).all()
        )

    if detail_data is not None:
        return detail_data
    else: 
        return None

def join_all(db = Session, id = int):
    header = get_header_data(db, id)
    detail = get_detail_data(db, id)

    getData = {}
    getData.update(header._asdict())
    getData['Items'] = [item._asdict() for item in detail]

    return getData
    
     


