from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message' : {'hello': 'world'}}

@app.get('/about')
def about():
    return {'data': 'about page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'this is unpublished page'}

@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {'comments': {'hi', 'hello'}}
