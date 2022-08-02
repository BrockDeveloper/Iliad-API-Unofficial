import requests
from lxml import html
from iliadrequests.models import *
from iliadrequests.routes import *
from iliadrequests.xpaths import *
from iliadrequests.exceptions import InvalidCredentials, NoToken, InvalidToken, BadRequest, InvalidXPath



def __get_header_info(token: str) -> dict:

    '''
    Returns the header for the request with the token

    PARAM: 
        token: the token to be used

    RETURN:
        the header for the request with the token
    '''

    HEADER_COOKIE = "ACCOUNT_SESSID="
    HEADER_INFO = {'cookie' : ""}

    HEADER_INFO['cookie'] = HEADER_COOKIE + token
    return HEADER_INFO



def __invalid_token(response_content: str) -> bool:

    '''
    Checks if the token is invalid
    
    PARAM:
        response_content: the response content from the request
        
    RETURN:
        True if the token is invalid, False otherwise
    '''

    invalid_login = "ID utente o password non corretto."
    invalid_token = "Accedi alla tua area personale iliad per gestire la tua offerta"

    return (invalid_login in str(response_content)) or (invalid_token in str(response_content))



def get_auth_token(username: str, password: str) -> str:

    '''
    Returns the token generated by the user's login
    
    PARAM:
        username: the username for the login
        password: the password for the login
        
    RETURN:
        the token for the user
        
    RAISE:
        InvalidCredentials, if the login credentials are invalid
        NoToken, if the token is not generated
        BadRequest, if the request is not OK
    '''

    LOGIN_INFO = {'login-ident': '', 'login-pwd': ''}
    LOGIN_INFO['login-ident'] = username
    LOGIN_INFO['login-pwd'] = password

    with requests.session() as request:

        try:
            response = request.post(MAIN_URL, data=LOGIN_INFO)
        except Exception:
            raise BadRequest()

        if(not response.ok):
            raise BadRequest()

        if __invalid_token(response.content):
            raise InvalidCredentials()

        if request.cookies.get('ACCOUNT_SESSID'):
            return Authorization(id = username, token = request.cookies.get_dict()['ACCOUNT_SESSID'])
        else:
            raise NoToken()



def __get_xpath_request(token:str, url: str, xpath: str) -> list:
    
    '''
    Looks for the values ​​specified by xpath in the response
    
    PARAM:
        token: the token to be used
        url: the url of the request
        xpath: the xpath to be used
        
    RETURN:
        the requested values searched with the xpath in the response
        
    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
    '''

    try:
        response = requests.post(url, headers=__get_header_info(token))
    except Exception:
        raise BadRequest()

    if(not response.ok):
        raise BadRequest()

    if __invalid_token(response.content):
        raise InvalidToken()

    try:
        tree = html.fromstring(response.content)
        return tree.xpath(xpath)
    except Exception:
        raise InvalidXPath()



def get_conversation_time(token: str):

    '''
    Returns the conversation time of the user

    PARAM:
        token: the token to be used

    RETURN:
        the conversation time of the user

    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''

    response = __get_xpath_request(token, MAIN_URL, CONV_TIME)[0]

    if not response:
        raise InvalidXPath()

    response = response.split(' ')
    conv_time = ConversationTime()
    conv_time.parse_init(response)
    return conv_time



def get_sent_messages(token: str) -> str:

    '''
    Returns the sent messages from the user

    PARAM:
        token: the token to be used
    
    RETURN:
        the sent messages from the user

    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''

    response = __get_xpath_request(token, MAIN_URL, SENT_MSG)[0]
    response = response.split(' ')
    return SentMessages(sent = response[0])



def get_used_traffic(token: str) -> str:

    '''
    Returns the user's internet traffic

    PARAM:
        token: the token to be used
    
    RETURN:
        the user's internet traffic
    
    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''

    response = __get_xpath_request(token, MAIN_URL, USED_TRAFFIC)[0]
    return UsedTraffic(unit = response[-2:], used = float(response[:-2].replace(',', '.')))



def get_max_traffic(token: str) -> str:

    '''
    Returns the maximum internet traffic available to the user
    
    PARAM:
        token: the token to be used
    
    RETURN:
        the max traffic from the request with the token
    
    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''
    
    response = __get_xpath_request(token, MAIN_URL, MAX_TRAFFIC)[1]
    return MaxTraffic(unit = response[-2:], max = float(response[:-2].replace('/', '').strip()))



def get_traffic(token: str) -> str:

    '''
    Returns all information on internet traffic
    
    PARAM:
        token: the token to be used
    
    RETURN:
        all information on internet traffic
    
    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''
    
    return Traffic(used_traffic = get_used_traffic(token), max_traffic = get_max_traffic(token))



def get_renewal_date(token: str) -> str:

    '''
    Returns the renewal date of the active offer
    
    PARAM:
        token: the token to be used
    
    RETURN:
        the renewal date of the active offer
        
    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''

    response = __get_xpath_request(token, MAIN_URL, RENEWAL)[0]
    response = response.strip().split(' ')
    return RenewalDate(date=response[9], time=response[7])



def get_all_user_data(token: str):

    '''
    Returns all information on the user

    PARAM:
        token: the token to be used
    
    RETURN:
        all information on the user
    
    RAISE:
        InvalidToken, if the token is invalid
        BadRequest, if the request is not OK
        invalid_xpath, if the xpath is invalid
    '''
    
    return AllUserData(conversation_time=get_conversation_time(token), sent_messages=get_sent_messages(token), traffic=get_traffic(token), renewal_date=get_renewal_date(token))