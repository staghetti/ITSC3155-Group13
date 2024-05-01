from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)  # Links to a customer if not a guest
    customer_name = Column(String(100))
    description = Column(String(300))
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    is_guest = Column(Boolean, default=True, nullable=False)
    order_type = Column(Enum("Takeout", "Delivery", "Dine-In", name="order_types"), default="Dine-In", nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")
