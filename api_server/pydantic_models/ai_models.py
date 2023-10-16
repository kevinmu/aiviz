from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    ACTIVE = 'ACTIVE'
    DEPRECATED = 'DEPRECATED'
    IN_DEVELOPMENT = 'IN_DEVELOPMENT'
    RUMORED = 'RUMORED'

class ModelResponse(BaseModel):
    id: str
    name: Optional[str]
    description: Optional[str]
    num_parameters: Optional[int]
    release_date: Optional[datetime.date]
    architecture: Optional[str]
    license: Optional[str]
    developed_by: Optional[str]
    status: Optional[StatusEnum]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class CreateModelInput(BaseModel):
    name: str
    description: str
    num_parameters: int
    release_date: str
    architecture: str
    license: str
    developed_by: str
    status: str

class DeleteModelResponse(BaseModel):
    message: str
