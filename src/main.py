import uvicorn
from fastapi import FastAPI, APIRouter

from api.auth.router import router as auth_router
from api.tasks.router import router as tasks_router


main_router = APIRouter()
main_router.include_router(auth_router)
main_router.include_router(tasks_router)


app = FastAPI(docs_url="/api/docs")
app.include_router(main_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0",
        port=8000,
        ssl_keyfile='ssl/localhost+2-key.pem',
        ssl_certfile='ssl/localhost+2.pem'
    )
