from pydantic import BaseModel



class AuthRequest(BaseModel):

    '''
    Request body for the authorization endpoint.
    
    ATTRIBUTES:
        username: login username
        password: login password
    '''

    username: str
    password: str



class Token(BaseModel):

    '''
    Response body for the authorization endpoint.

    ATTRIBUTES:
        token: authorization token
    '''
    
    token: str