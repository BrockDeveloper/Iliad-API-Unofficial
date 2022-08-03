from fastapi import FastAPI
from backend.routes import router
from backend.jsendstd import ErrorResponse
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import RequestValidationError
from params import API_NAME, API_VERSION, API_DESC, API_LOGO



# fastapi application
app = FastAPI()
app.include_router(router)



# custom generic exception handler for all processes problems
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code = 422, content = ErrorResponse(message = "Unprocessable Entity, check your request").dict())



# custom openapi specification
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(title = API_NAME, version = API_VERSION, description = API_DESC, routes = app.routes,)
    openapi_schema["info"]["x-logo"] = {"url": API_LOGO}
    app.openapi_schema = openapi_schema

    return app.openapi_schema

app.openapi = custom_openapi