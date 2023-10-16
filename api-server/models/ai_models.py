from pydantic import BaseModel

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
