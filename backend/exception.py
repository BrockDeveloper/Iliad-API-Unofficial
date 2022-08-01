from fastapi.responses import JSONResponse
from iliadrequests.exceptions import *



def parse_exception(exception: Exception):

    '''
    This function is used to parse the exception and return a JSONResponse with the error message.
    
    PARAM:
        exception: The exception that was raised.
    
    RETURN:
        A JSONResponse with the error message.
    '''

    if isinstance(exception, InvalidCredentials | NoToken | InvalidToken):
        return JSONResponse(status_code = 401, content = {"error": str(exception)})

    if isinstance(exception, BadRequest):
        return JSONResponse(status_code = 400, content = {"error": str(exception)})

    if isinstance(exception, InvalidXPath):
        return JSONResponse(status_code = 500, content = {"error": str(exception)})

    return JSONResponse(status_code=500, content={'Error': "Internal server error"})