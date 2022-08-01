from fastapi import APIRouter, status
from backend.body import AuthRequest
from iliadrequests.models import Authorization
from iliadrequests.requests import get_auth_token


router = APIRouter(prefix = "/iliadapi")

@router.get("/authorization", response_model = Authorization, status_code = status.HTTP_200_OK)
def get_authorization(auth_request: AuthRequest):
    return get_auth_token(auth_request.username, auth_request.password)