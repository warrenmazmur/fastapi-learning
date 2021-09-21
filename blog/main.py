from typing import final
from fastapi import FastAPI, Depends
from . import schemas, models
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create new blog and insert to db
@app.post('/blog')
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# get all blog in db
@app.get('/blog')
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# get specific blog with id == id
@app.get('/blog/{id}')
def get_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog
