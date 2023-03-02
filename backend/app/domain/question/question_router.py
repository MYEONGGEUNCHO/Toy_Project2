from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional

# from db.database import SessionLocal
from db.database import get_db
from domain.question import question_schema, question_crud
from models.models import Question

router = APIRouter(
    prefix="/api/question"
)

# @router.get("/list")
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
#     db.close()
    
#     return _question_list

# @router.get("/list")
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
#     return _question_list

# @router.get("/list")
@router.get("/list", response_model=List[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)
    
    return _question_list