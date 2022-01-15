import os
from twilio.rest import Client

def get_logs():
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = 'ACCOUNT_SID'
    auth_token = 'AUTHTOKEN'
    client = Client(account_sid, auth_token)

    calls = client.calls.list(limit=20)
    
    return calls
