from create_db import Project, session, Base
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker

def fetch_projects():
    projects = session.query(Project).all()
    return projects

def delete_project(project_id):
    project = session.query(Project).filter(Project.id == project_id).one()
    session.delete(project)
    session.commit()



engine = create_engine('sqlite:///sewing.db', echo=True)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def search_projects(keyword):
    return session.query(Project).filter(
        or_(
            Project.name.contains(keyword),
            Project.tags.contains(keyword)
        )
    ).all()
