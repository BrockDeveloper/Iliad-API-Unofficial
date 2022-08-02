class IliadRequestsException(Exception):

    '''
    Generic exception for IliadRequests.
    '''

    def __init__(self):
        self.message = "An exception occurred"

    def __str__(self):
        return self.message



class InvalidCredentials(IliadRequestsException):

    '''
    Raised when the username or password is invalid.
    '''

    def __init__(self):
        self.message = "Invalid username or password"



class NoToken(IliadRequestsException):

    '''
    Raised when the token is not found in the session.
    '''

    def __init__(self):
        self.message = "No token generated"



class InvalidToken(IliadRequestsException):

    '''
    Raised when the token is invalid.
    '''

    def __init__(self):
        self.message = "Invalid token"



class BadRequest(IliadRequestsException):

    '''
    Raised when the request is bad.
    '''

    def __init__(self):
        self.message = "Bad request"



class InvalidXPath(IliadRequestsException):

    '''
    Raised when the xpath is invalid.
    '''
    
    def __init__(self):
        self.message = "Invalid xpath"