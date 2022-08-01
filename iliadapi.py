from fastapi import FastAPI
import uvicorn
from backend.routes import router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app = FastAPI()
origins = ["http://localhost:8000"]

app.include_router(router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={'error': "Unprocessable Entity, check your request"})


if __name__ == '__main__':
    uvicorn.run("iliadapi:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")