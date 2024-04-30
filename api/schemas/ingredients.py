from typing import Optional
from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str
    amount: int


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    amount: Optional[int] = None


class Ingredient(IngredientBase):
    id: int

    class ConfigDict:
        from_attributes = True
