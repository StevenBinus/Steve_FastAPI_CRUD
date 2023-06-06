from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal
import datetime

class detail_schema(BaseModel):
    ItemCode: str
    ItemName: str   
    QtyDemand: Decimal
    ItemPrice: Decimal
    DiscPercent: Decimal
    DiscAmount: Decimal
    LineTotal:Decimal
    QtySupplied: Decimal

    class config:
        orm_mode = True

class header_schema(BaseModel):
    SOSysNo: int
    SODocNo: str
    SODate: datetime.date
    SOStatus: str
    CustomerCode: str
    CustomerName: str
    CustomerAddress: str
    CustomerMobilePhoneNo: str
    TOP: str
    TotalAmount: Decimal
    SalesEmployeeNo: Optional[str] = None
    SalesEmployeeName: Optional[str]
    Items:Optional[List[detail_schema]] = []

    class config:
        orm_mode = True


