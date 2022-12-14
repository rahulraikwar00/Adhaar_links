from dataclasses import field
from typing import Optional,Union
import datetime
from xml.dom.minicompat import defproperty
from sqlmodel import Field, SQLModel

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    username: Union[str, None] = None

# class User(SQLModel): #User registeration form
#     username: str
#     password:str 
#     confirmpass: str
#     disabled: Union[bool, None] = None

class agency(SQLModel): #organisation registeration form
    agency_Name:str
    ag_uniq_id:str   #(ifsc if bank else its uniqueid)
    password:str
    cnfpass:str

class user_req_agency_form(SQLModel): 
    Adhaar:str
    ag_uniq_id:str
    custid:str

class response_form(SQLModel):
    request_id : str
    status : str