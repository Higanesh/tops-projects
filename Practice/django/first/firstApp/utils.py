import requests
from django.conf import settings

def send_sms(phone_number, message):
    url = "https://api.msg91.com/api/v5/flow/"
    
    headers = {
        "authkey": settings.MSG91_AUTH_KEY,
        "Content-Type": "application/json",
    }
    
    payload = {
        "flow_id": "your_flow_id",  # If using MSG91 Flow, else use the basic API
        "sender": settings.MSG91_SENDER_ID,
        "recipients": [{"mobiles": f"{settings.MSG91_COUNTRY_CODE}{phone_number}"}],
        "variables": {"VAR1": message}  # If using Flow
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
