from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from routers import router
from pages.router import router as pages_router

app = FastAPI(title='ScanPatrol', redoc_url=None)

origins = ['http://localhost:3000', 'http://127.0.0.1:3000',
           'https://localhost:3000', 'https://127.0.0.1:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(router)
app.include_router(pages_router)

@app.exception_handler(RequestValidationError)
async def RequestValidationError_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        status_code=406,
        content='Неверный ввод данных. Вернитесь назад и повторите попытку'
    )