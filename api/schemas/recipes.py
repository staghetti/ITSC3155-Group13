from typing import Optional
from pydantic import BaseModel


class RecipeBase(BaseModel):
    menu_item_id: int
    ingredient_id: int
    amount: float


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    menu_item_id: Optional[int] = None
    ingredient_id: Optional[int] = None
    amount: Optional[float] = None


class Recipe(RecipeBase):
    id: int

    class ConfigDict:
        from_attributes = True
