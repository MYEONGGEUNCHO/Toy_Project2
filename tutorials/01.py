'''
uvicorn 01:app --reload
'''
'''
First Steps
'''

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}