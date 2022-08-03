from iliadrequests.exceptions import *
from fastapi.responses import JSONResponse
from backend.jsendstd import ErrorResponse



def parse_exception(exception: Exception):

    '''
    This function is used to parse the exception and return a JSONResponse with the error message.
    
    PARAM:
        exception: The exception that was raised.
    
    RETURN:
        A JSONResponse with the error message.
    '''

    if isinstance(exception, InvalidCredentials | NoToken | InvalidToken):
        return JSONResponse(status_code = 401, content = ErrorResponse(message = str(exception)).dict())

    if isinstance(exception, BadRequest):
        return JSONResponse(status_code = 400, content = ErrorResponse(message = str(exception)).dict())

    if isinstance(exception, InvalidXPath):
        return JSONResponse(status_code = 500, content = ErrorResponse(message = str(exception)).dict())

    return JSONResponse(status_code=500, content = ErrorResponse(message = "Internal server error").dict())