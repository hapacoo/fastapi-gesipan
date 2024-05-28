from sqlalchemy import create_engine, MetaData  #DB엔진 생성을 위한 함수
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base #SQLAlchemy의 선언형 모델을 사용하기 위한 클래스와 함수
from sqlalchemy.orm import sessionmaker #DB세션을 생성하고 관리하는 클래스

DATABASE_URL = "sqlite:///test.db"
#사용할 DB의 주소를 설정
engine = create_engine(DATABASE_URL) #SQL쿼리를 DB에 전달
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#autocommit=False: 자동 커밋을 비활성화, autoflush=False:자동 플러시를 비활성화, bind=engine: 생성한 세션 클래스가 사용할 DB 엔진을 지정
Base: DeclarativeMeta = declarative_base()
#declarative_base 함수를 사용해 모든 모델이 상속받을 기본 클래스 'Base'를 생성

#@contextlib.contextmanager #어노테이션?
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)
def get_db(): #db세션 객체를 리턴하는 제너레이터 함수
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
