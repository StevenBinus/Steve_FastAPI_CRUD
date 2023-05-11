from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal
import datetime

class detail_model(BaseModel):
    ItemCode: str
    ItemName: str
    QtyDemand: str
    ItemPrice: Decimal
    DiscPercent: Decimal
    DiscAmount: Decimal
    LineTotal:Decimal
    QtySupplied: Decimal

class header_model(BaseModel):
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
    SalesemployeeName: str
    Items:List[detail_model]
