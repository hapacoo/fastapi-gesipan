from models import Question
from sqlalchemy.orm import Session
from datetime import datetime
from domain.question.question_schema import QuestionCreate, QuestionUpdate

def get_question_list(db:Session, skip: int=0, limit: int=10):
    _question_list = db.query(Question).order_by(Question.create_date.desc())
    total = _question_list.count()
    question_list = _question_list.offset(skip).limit(limit).all()
    return total, question_list

def get_question(db:Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question

def create_question(db:Session, question_create: QuestionCreate):
    db_question = Question(subject=question_create.subject,
                           content = question_create.content,
                           create_date = datetime.now())
    db.add(db_question)
    db.commit()

def update_question(db:Session, db_question: Question, question_update: QuestionUpdate):
    db_question.subject = question_update.subject
    db_question.content = question_update.content
    db_question.modify_date = datetime.now() #수정일시도 확인
    db.add(db_question)
    db.commit()