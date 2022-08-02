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



class __Unit(BaseModel):

    '''
    Unit Model

    ATTRIBUTES:
        name: name of the unit
    '''

    unit: str



class UsedTraffic(__Unit):

    '''
    Used traffic Model

    ATTRIBUTES:
        used: used traffic
        unit: used traffic unit
    '''

    used: float



class MaxTraffic(__Unit):

    '''
    Max traffic Model
    
    ATTRIBUTES:
        max: max traffic
        unit: max traffic unit
    '''

    max: float



class Traffic(BaseModel):

    '''
    Traffic Model

    ATTRIBUTES:
        used_traffic: used traffic [Model see: UsedTraffic]
        max_traffic: max traffic [Model see: MaxTraffic]
    '''

    used_traffic: UsedTraffic
    max_traffic: MaxTraffic



class RenewalDate(BaseModel):

    '''
    Renewal date Model

    ATTRIBUTES:
        date: renewal date
        time: renewal time
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
        if isinstance(value, date):
            return value
        else:
            return datetime.strptime(value, "%d/%m/%Y").date()



class AllUserData(BaseModel):

    '''
    All user data Model

    ATTRIBUTES:
        conversation_time: conversation time [Model see: ConversationTime]
        sent_messages: sent messages [Model see: SentMessages]
        traffic: traffic [Model see: Traffic]
        renewal_date: renewal date [Model see: RenewalDate]
    '''

    conversation_time : ConversationTime
    sent_messages : SentMessages
    traffic : Traffic
    renewal_date : RenewalDate