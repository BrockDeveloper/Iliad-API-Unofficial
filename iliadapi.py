from fastapi import FastAPI
import uvicorn
from backend.routes import router

app = FastAPI()
origins = ["http://localhost:8000"]

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run("iliadapi:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")