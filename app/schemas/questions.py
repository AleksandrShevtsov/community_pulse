from typing import Optional
from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: Optional[int]
    name: str = Field(..., min_length=2, max_length=100)

    class Config:
        model_config = {'from_attributes': True}


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: Optional[int]


class QuestionResponse(BaseModel):
    text: str
    category: Optional[CategoryBase]

    class Config:
        # Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        model_config = {'from_attributes': True}


class MessageResponse(BaseModel):
    message: str

    class Config:
        from_attributes = True
