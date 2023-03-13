import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.answer import answer_router
from domain.question import question_router
from domain.user import user_router
from domain.engine.leverage import leverage_router

from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME
    , openapi_url=f'{settings.API_ENTRYPOINT}/openapi.json'
)

origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/hello")
def hello():
    return {"message": "Hello World"}

app.include_router(question_router.router, tags=['Question'])
app.include_router(answer_router.router, tags=['Answer'])
app.include_router(user_router.router, tags=['Users'])
app.include_router(leverage_router.router, tags=['Levarage'])

if __name__ == '__main__':
    uvicorn.run(
        "main:app"
        , host=settings.HOST
        , port=settings.PORT
        
        # , debug=settings.DEBUG
        , reload=settings.DEBUG
    )