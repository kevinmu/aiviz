from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from db_models.ai_model import AIModel

def get_model(db: Session, id: str) -> AIModel:
    db_model = db.query(AIModel).filter(AIModel.id == id).first()
    if db_model is None:
        raise HTTPException(status_code=404, detail="AIModel not found")
    return db_model

def get_models(db: Session, first: int, after: int) -> List[AIModel]:
    db_model = db.query(AIModel).offset(after).limit(limit).all()

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

