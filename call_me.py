# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os



# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get('twilio-sid')
auth_token = os.environ.get('twilio-token')
client = Client(account_sid, auth_token)

kiraa = '+421910922660'
mlpard = '+421949294672'

def call_someone(num):
    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to=num,
                            from_='+421233057068'
                        )

    print(call.sid)

def call_people_to_alert():
    call_someone(kiraa)
    #call_someone(mlpard)

