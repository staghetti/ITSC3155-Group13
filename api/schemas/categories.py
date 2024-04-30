from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None


class Category(CategoryBase):
    id: int
