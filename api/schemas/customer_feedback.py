from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel


class FeedbackBase(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None
    rating: Optional[float] = None


class FeedbackCreate(FeedbackBase):
    pass


class FeedbackUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None
    rating: Optional[float] = None


class Feedback(FeedbackBase):
    id: int
    order_date: Optional[datetime] = None

    class ConfigDict:
        from_attributes = True
