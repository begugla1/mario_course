import uvicorn
from fastapi import FastAPI, APIRouter

from auth.router import router as auth_router


main_router = APIRouter()
main_router.include_router(auth_router)


app = FastAPI(openapi_url="/api/docs")
app.include_router(main_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
