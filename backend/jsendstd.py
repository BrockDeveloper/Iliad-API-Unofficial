from typing import Any
from pydantic import BaseModel
from iliadrequests.models import *


class SuccessResponse(BaseModel):
    status = "success"
    data: Any


class ErrorResponse(BaseModel):
    status = "error"
    message: str