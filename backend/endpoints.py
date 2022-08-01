from fastapi import APIRouter, status
from backend.body import AuthRequest, Token
from backend.exception import parse_exception
from iliadrequests.models import Authorization, ConversationTime, RenewalDate, SentMessages, Traffic
import iliadrequests.requests as iliad
from iliadrequests.exceptions import IliadRequestsException


router = APIRouter(prefix = "/iliadapi")



@router.get("/authorization", response_model = Authorization, status_code = status.HTTP_200_OK)
def get_authorization(auth_request: AuthRequest):
    try:
        return iliad.get_auth_token(auth_request.username, auth_request.password)
    except IliadRequestsException as exception:
        return parse_exception(exception)


@router.get("/conversation-time", response_model = ConversationTime, status_code = status.HTTP_200_OK)
def get_conversation_time(token: Token):
    try:
        return iliad.get_conversation_time(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)


@router.get("/sent-messages", response_model = SentMessages, status_code = status.HTTP_200_OK)
def get_sent_messages(token: Token):
    try:
        return iliad.get_sent_messages(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)


@router.get("/internet-traffic", response_model = Traffic, status_code = status.HTTP_200_OK)
def get_internet_traffic(token: Token):
    try:
        return iliad.get_traffic(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)


@router.get("/renewal-date", response_model = RenewalDate, status_code = status.HTTP_200_OK)
def get_renewal_date(token: Token):
    try:
        return iliad.get_renewal_date(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)