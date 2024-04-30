from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    description = Column(String(1000))
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    rating = Column(Float, nullable=False)
    __table_args__ = (CheckConstraint('rating>=1 AND rating<=5', name='rating_range'),)
    customer = relationship("Customer", back_populates="feedbacks")
