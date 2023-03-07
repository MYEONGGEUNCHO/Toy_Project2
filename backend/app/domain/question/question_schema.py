import datetime
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

class Question(BaseModel):
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers: List[Answer] = []
    user: User
    modify_date: datetime.datetime = None
    voter: List[User] = []
    
    class Config:
        orm_mode = True
        

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class QuestionList(BaseModel):
    total: int = 0
    question_list: List[Question] = []
    
class QuestionUpdate(QuestionCreate):
    question_id: int
    
class QuestionDelete(BaseModel):
    question_id: int
    
class QuestionVote(BaseModel):
    question_id: int