from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}


@app.get('/user')
def user():
    return "{'email': 'pxr@gmail.com', 'age': 20}"



if __name__ == '__main__':
    uvicorn.run("api:app", reload=True)