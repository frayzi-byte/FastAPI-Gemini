from db import session, ChatRequests
from sqlalchemy import select

def get_user_requests(ip_adrr : str):
    with session() as new_session:
        query = select(ChatRequests).filter_by(ip_adrr=ip_adrr)
        result = new_session.execute(query)
        return result.scalars().all()

def add_request_data(ip_adrr : str, promt : str, response : str):
    with session() as new_session:
        new_request = ChatRequests(
            ip_adrr = ip_adrr,
            promt = promt,
            response=response,
        )
        new_session.add(new_request)
        new_session.commit()