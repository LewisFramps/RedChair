
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC067e3bc62e3e81c5224f3be10ea88974'
auth_token = 'dbb987b17739978a915693a8b643e599'
client = Client(account_sid, auth_token)

numbers_to_message = ['+447930742804', '+447930742804']
for number in numbers_to_message:
    client.messages.create(
        body = 'Hello from my Twilio number!',
        from_ = '+447700155318',
        to = number
    )
    #print(m.sid)
"""
message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='++447700155318',
         to='+447930742804'
     )
"""
print(message.sid)
