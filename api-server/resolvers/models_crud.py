from fastapi import HTTPException
from sqlalchemy.orm import Session
from db_models import AIModel

def read_model(db: Session, id: str) -> AIModel:
    db_model = db.query(AIModel).filter(AIModel.id == id).first()
    if db_model is None:
        raise HTTPException(status_code=404, detail="AIModel not found")
    return db_model

def create_model(db: Session, model: AIModel) -> AIModel:
    db.add(model)
    db.commit()
    db.refresh(model)
    return model

def delete_model(db: Session, id: str):
    db_model = db.query(AIModel).filter(AIModel.id == id).first()
    if db_model is None:
        raise HTTPException(status_code=404, detail="AIModel not found")
    db.delete(db_model)
    db.commit()

