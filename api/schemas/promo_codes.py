from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoCodeBase(BaseModel):
    promo_code: str
    discount_amount: float
    start_date: datetime
    end_date: datetime
    is_active: bool = True


class PromoCodesCreate(PromoCodeBase):
    pass


class PromoCodesUpdate(BaseModel):
    discount_amount: Optional[float] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class PromoCode(PromoCodeBase):
    id: int
    order_id: int = None
    order_date: datetime = None

    class ConfigDict:
        from_attributes = True
