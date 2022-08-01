from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, time, datetime



class Authorization(BaseModel):
    '''
    Authorization model
    
    Attributes:
        id: given user id
        token: generated user token
    '''

    id: str
    token: str



class ConversationTime(BaseModel):

    '''
    Conversation time Model

    ATTTRIBUTES:
        h: hours of conversation
        m: minutes of conversation
        s: seconds of conversation
    '''

    h: Optional[int] = 0
    m: Optional[int] = 0
    s: Optional[int] = 0


    def parse_init(self, time: list):

        '''
        Parses the time from the list given by the xpath request

        PARAM:
            time: the list of strings to be parsed
        
        RETURN:
            None
        '''

        for unit in time:
            setattr(self, unit[-1], int(unit[:-1]))



class SentMessages(BaseModel):

    '''
    Sent messages Model
    
    ATTRIBUTES:
        sent: number of sent messages
    '''

    sent: int



class UsedTraffic(BaseModel):

    '''
    Used traffic Model

    ATTRIBUTES:
        used: used traffic
        used_unit: used traffic unit
    '''

    used_unit: str
    used: float



class MaxTraffic(BaseModel):

    '''
    Max traffic Model
    
    ATTRIBUTES:
        max: max traffic
        max_unit: max traffic unit
    '''

    max_unit: str
    max: float



class Traffic(UsedTraffic, MaxTraffic):

    '''
    Traffic Model

    ATTRIBUTES:
        used: used traffic
        used_unit: used traffic unit
        max: max traffic
        max_unit: max traffic unit
    '''

    pass



class RenewalDate(BaseModel):

    '''
    Renewal date Model

    ATTRIBUTES:
        day: day of renewal
        month: month of renewal
        year: year of renewal
    '''

    date: date
    time: time


    @validator("date", pre=True)
    def parse_date(cls, value):

        '''
        Parses the date from the string given by the xpath request
        
        PARAM:
            value: the string to be parsed
        
        RETURN:
            the parsed date
        '''
        
        return datetime.strptime(value, "%d/%m/%Y").date()