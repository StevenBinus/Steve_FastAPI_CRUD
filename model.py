from connection.Connection import Base

from sqlalchemy import ForeignKey, Integer, String, Float, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from typing import List, Optional

class Base(DeclarativeBase):
    pass

class detail_model(Base):
    __tablename__ = 'atSalesOrder1'
    
    SO_LINE_NUMBER = Column(Integer, primary_key=True)
    ITEM_CODE = Column(String)
    QTY_DEMAND = Column(Float)
    PRICE = Column(Float)
    DISC_PERCENT = Column(Float)
    DISC_AMOUNT = Column(Float)
    DISC_REQ_AMOUNT = Column(Float)
    QTY_SUPPLY = Column(Float)
    SO_SYS_NO = Column(Integer, ForeignKey('atSalesOrder0.SO_SYS_NO'))
    header: Mapped['header_model'] = relationship(back_populates = 'items')

class header_model(Base):
    __tablename__ = 'atSalesOrder0'

    SO_SYS_NO = Column(Integer, primary_key=True)
    SO_DOC_NO = Column(String)
    SO_DATE = Column(DateTime)
    SO_STATUS = Column(String)
    CUST_CODE = Column(String, ForeignKey('gmCust0.CUSTOMER_CODE'))
    DLVR_ADDR = Column(String)
    DLVR_ADDR1 = Column(String)
    DLVR_ADDR2 = Column(String)
    TOP_CODE = Column(String)
    TOTAL = Column(Integer)
    SALES_EMP_NO = Column(Integer, ForeignKey('gmEmp.EMPLOYEE_NO'))
    ITEM = Column(String)
    items: Mapped[List['detail_model']] = relationship(back_populates='header')
    
class customer_model(Base):
    __tablename__ = 'gmCust0'

    CUSTOMER_CODE = Column(String, primary_key=True)
    CUSTOMER_NAME = Column(String)
    CUST_MOBILE_PHONE = Column(String)

class sales_employee_model(Base):
    __tablename__ = 'gmEmp'

    EMPLOYEE_NO = Column(String, primary_key=True)
    EMPLOYEE_NAME = Column(String)

class item_model(Base):
    __tablename__ = 'gmitem0'

    ITEM_CODE = Column(String, primary_key=True)
    ITEM_NAME = Column(String)
