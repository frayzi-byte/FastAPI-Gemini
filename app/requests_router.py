from fastapi import APIRouter, Body, Request
from gemini_client import get_answer_from_gemini
from requests_repositories import get_user_requests, add_request_data

router = APIRouter(prefix="/requests")

@router.get("/")
def get_my_requests(request : Request):
    user_ip_adress = request.client.host
    response = get_user_requests(ip_adrr=user_ip_adress)
    return response

@router.post("/")
def send_promt(request : Request, promt : str = Body(embed=True)):
    answer = get_answer_from_gemini(promt)
    user_ip_adress = request.client.host
    add_request_data(ip_adrr=user_ip_adress, promt=promt, response=answer)
    return {"answer" : answer}