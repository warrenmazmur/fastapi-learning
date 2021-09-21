from fastapi import FastAPI
from typing import Optional
from models.blog import Blog

app = FastAPI()

@app.get('/')   
def index():
    return {'message' : {'hello': 'world'}}

@app.get('/about')
def about():
    return {'data': 'about page'}

@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get {limit} {published} blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'this is unpublished page'}

@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'comments': {'hi', 'hello'}}

@app.post('/blog')
def create_blog(request: Blog):
    return request
    return {'data': f'Blog is created with title "{request.title}"'}