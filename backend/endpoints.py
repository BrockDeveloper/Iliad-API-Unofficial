from fastapi import APIRouter, status
from backend.body import AuthRequest, Token
from iliadrequests.models import Authorization, ConversationTime, RenewalDate, SentMessages, Traffic
import iliadrequests.requests as iliad


router = APIRouter(prefix = "/iliadapi")

@router.get("/authorization", response_model = Authorization, status_code = status.HTTP_200_OK)
def get_authorization(auth_request: AuthRequest):
    return iliad.get_auth_token(auth_request.username, auth_request.password)


@router.get("/conversation_time", response_model = ConversationTime, status_code = status.HTTP_200_OK)
def get_conversation_time(token: Token):
    return iliad.get_conversation_time(token.token)


@router.get("/sent_messages", response_model = SentMessages, status_code = status.HTTP_200_OK)
def get_sent_messages(token: Token):
    return iliad.get_sent_messages(token.token)


@router.get("/internet_traffic", response_model = Traffic, status_code = status.HTTP_200_OK)
def get_internet_traffic(token: Token):
    return iliad.get_traffic(token.token)


@router.get("/renewal_date", response_model = RenewalDate, status_code = status.HTTP_200_OK)
def get_renewal_date(token: Token):
    return iliad.get_renewal_date(token.token)