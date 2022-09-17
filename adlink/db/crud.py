from .database import *
from .crud import *
from .models import *
from .schemas import *
from sqlmodel import Session, select
import hashlib
from features.dropdown import *
from passlib.context import CryptContext
from uuid import uuid1
from fastapi.security import OAuth2PasswordRequestForm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = Session(engine)
    return db

# def add_ag_login(data:agency_data):
#     pass

def register_users(data:agency):
    with get_db() as db:
        ag = agency_data(ag_uniq_id = data.ag_uniq_id,agency_Name = data.agency_Name,hashedpass = pwd_context.hash(data.password))
        db.add(ag)
        # add_ag_login(ag)  #function to add login details of agency
        db.commit()

#get user data for authentication
def get_all_agencies()->dict:
    with get_db() as db:
        res = db.exec(
            "SELECT * FROM agency_data;"
        ).fetchall()
        return res

def getagid(agunid):
    with get_db() as db:
        res = db.exec(
            f"SELECT agency_id FROM agency_data WHERE ag_uniq_id = '{agunid}';"
        ).one()
        return res.agency_id

def syncUp(data:user_req_agency_form):
    with get_db() as db:
        agenid = getagid(data.ag_uniq_id)
        req = user_req_agency(agencyid = agenid,adhaar = data.Adhaar,custid = data.custid)
        db.add(req)
        db.commit()

def getreq():
    with get_db() as db:
        reqs = db.exec(
            "SELECT * FROM user_req_agency;"
        ).fetchall()
        return reqs

def res_data():
    return 0 #get response from agency

def ag_res(reqid):
    with get_db() as db:
        res = db.exec(
            f"SELECT * FROM user_req_agency WHERE reqid = '{reqid}';"
        ).fetchall()
        print(res)
        return res_data()
        
