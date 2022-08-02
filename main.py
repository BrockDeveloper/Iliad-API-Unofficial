import uvicorn
from fastapi import FastAPI
from backend.routes import router
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import RequestValidationError



app = FastAPI()


app.include_router(router)



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=422, content={'error': "Unprocessable Entity, check your request"})



def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Iliad UnAPI",
        version="1.0.0",
        description="Unofficial Iliad API. Iliad S.P.A. is not responsible in any way.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi



# if __name__ == '__main__':
#     uvicorn.run("iliadapi:app", host='192.168.178.43', port=8005, log_level="info", reload=True)
#     print("running")