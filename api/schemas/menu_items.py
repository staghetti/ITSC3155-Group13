from typing import Optional
from pydantic import BaseModel


class MenuItemsBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: Optional[int] = None


class MenuItemCreate(MenuItemsBase):
    pass


class MenuUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None


class MenuItem(MenuItemsBase):
    id: int

