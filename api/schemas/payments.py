from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PaymentBase(BaseModel):
    order_id: int
    customer_name: str
    total_price: float
    payment_method: str


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    order_id: Optional[int] = None
    customer_name: Optional[str] = None
    total_price: Optional[float] = None
    payment_method: Optional[str] = None


class Payment(PaymentBase):
    id: int
    order_id: int
    order_date: Optional[datetime] = None
    payment_method: str

    class ConfigDict:
        from_attributes = True
