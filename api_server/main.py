from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from db_config import SessionLocal
from db_models.ai_model import AIModel
from pydantic_models.ai_models import CreateModelInput, DeleteModelResponse, ModelResponse
from resolvers import models_crud

app = FastAPI()
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def root():
    return {"Hello": "World"}

@router.get("/models/{id}", response_model=ModelResponse)
def model(id: int, db: Session = Depends(get_db)) -> AIModel:
    return models_crud.read_model(db, id)

@router.post("/model/", response_model=ModelResponse)
def create_model(
    model: CreateModelInput, 
    db: Session = Depends(get_db)
) -> AIModel:
    db_model = AIModel(
        name=model.name,
        description=model.description,
        num_parameters=model.num_parameters,
        release_date=model.release_date,
        architecture=model.architecture,
        license=model.license,
        developed_by=model.developed_by,
        status=model.status,
    )
    return models_crud.create_model(db, db_model)

@router.delete("/model/{id}", response_model=DeleteModelResponse)
def delete_model(id: str, db: Session = Depends(get_db)):
    models_crud.delete_model(db, id)
    return DeleteModelResponse(
        message="Successfully deleted model"
    )

app.include_router(router, prefix="/api")
