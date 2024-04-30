from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    menu_item_id = Column(Integer, ForeignKey('menu_items.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    amount = Column(DECIMAL, nullable=False)  # Amount of the ingredient per dish

    menu_item = relationship("MenuItems", back_populates="recipes")
    ingredient = relationship("Ingredients", back_populates="recipes")
