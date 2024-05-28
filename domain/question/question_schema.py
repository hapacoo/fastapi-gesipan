import datetime
from pydantic import BaseModel, field_validator
from domain.answer.answer_schema import Answer

class Question(BaseModel): #pydantic의 BaseModel을 상속한 Question클래스==Question스키마
    id: int
    subject: str #|None=None으로 쓰면 None을 가질 수 있고 디폴트는 None이다
    content: str
    create_date: datetime.datetime
    answers: list[Answer] = []

class QuestionCreate(BaseModel):
    subject: str
    content: str

    @field_validator('subject', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class QuestionList(BaseModel):
    total: int = 0
    question_list: list[Question] = []

class QuestionUpdate(QuestionCreate):
    question_id: int