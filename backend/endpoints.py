from fastapi import APIRouter, status
import iliadrequests.requests as iliad
from backend.body import AuthRequest, Token
from backend.exception import parse_exception
from backend.jsendstd import SuccessResponse
from iliadrequests.exceptions import IliadRequestsException
from iliadrequests.models import Authorization, ConversationTime, RenewalDate, SentMessages, Traffic, AllUserData



router = APIRouter(prefix = "/iliadapi")



@router.post("/authorization", response_model = SuccessResponse, status_code = status.HTTP_200_OK)
def get_authorization(auth_request: AuthRequest):
    
    try:
        return SuccessResponse(data = iliad.get_auth_token(auth_request.username, auth_request.password))
    except IliadRequestsException as exception:
        return parse_exception(exception)



@router.post("/conversation-time", response_model = ConversationTime, status_code = status.HTTP_200_OK)
def get_conversation_time(token: Token):

    try:
        return iliad.get_conversation_time(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)



@router.post("/sent-messages", response_model = SentMessages, status_code = status.HTTP_200_OK)
def get_sent_messages(token: Token):

    try:
        return iliad.get_sent_messages(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)



@router.post("/internet-traffic", response_model = Traffic, status_code = status.HTTP_200_OK)
def get_internet_traffic(token: Token):

    try:
        return iliad.get_traffic(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)



@router.post("/renewal-date", response_model = RenewalDate, status_code = status.HTTP_200_OK)
def get_renewal_date(token: Token):

    try:
        return iliad.get_renewal_date(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)



@router.post("/user-data", response_model = AllUserData, status_code = status.HTTP_200_OK)
def get_all_user_data(token: Token):

    try:
        return iliad.get_all_user_data(token.token)
    except IliadRequestsException as exception:
        return parse_exception(exception)