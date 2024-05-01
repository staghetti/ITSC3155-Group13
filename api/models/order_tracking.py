from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderTracking(Base):
    __tablename__ = "order_tracking"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tracking_number = Column(String(100), unique=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    status = Column(String(50), nullable=False)
    order = relationship("Order", back_populates="tracking")
