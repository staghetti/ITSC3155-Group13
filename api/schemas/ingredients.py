from typing import Optional
from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str


class IngredientCreate(IngredientBase):
    inventory_quantity: int


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    inventory_quantity: Optional[int] = None


class Ingredient(IngredientBase):
    id: int
    inventory_quantity: int

    class ConfigDict:
        from_attributes = True
