from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    start_date = Column(String(250))
    end_date = Column(String(250))
    reference_type = Column(String(250))
    reference_page_num = Column(Integer)
    size = Column(String(250))
    thread_used = Column(String(250))
    wearing_sensation = Column(String(250))
    tags = Column(String(250))
    difficulty_level = Column(String(250))

class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship(Project)
    image = Column(String(250))
    texture = Column(String(250))
    quantity = Column(Integer)

class FinishedImage(Base):
    __tablename__ = 'finished_images'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship(Project)
    image = Column(String(250))

# SQLiteデータベースを作成します
engine = create_engine('sqlite:///sewing.db')

# テーブルを作成します
Base.metadata.create_all(engine)

# セッションを作成します
DBSession = sessionmaker(bind=engine)
session = DBSession()

# データベースを扱うセッションができました。
# ここにデータを追加したり、検索したり、削除したりするコードを書くことができます。
