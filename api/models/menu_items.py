from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class MenuItems(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(DECIMAL(5, 2))
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Relationships to link menu items back to categories and to order details
    category = relationship("Category", back_populates="menu_items")
    order_details = relationship("OrderDetail", back_populates="menu_item")

    recipes = relationship("Recipe", back_populates="menu_item")
