from typing import Any
from pydantic import BaseModel
from iliadrequests.models import *



class SuccessResponse(BaseModel):

    '''
    Success response model
    
    ATTRIBUTES:
        status: Status of the response (success)
        data: Data of the response
    '''

    status = "success"
    data: Any



class ErrorResponse(BaseModel):

    '''
    Error response model

    ATTRIBUTES:
        status: Status of the response (error)
        message: Message of the error
    '''

    status = "error"
    message: str