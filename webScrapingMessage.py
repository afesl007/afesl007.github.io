from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

url = 'https://afesl007.github.io/'
# Your Account SID from twilio.com/console
account_sid = "######################"
# Your Auth Token from twilio.com/console
auth_token  = "########################"

twilio_phone_number = '+12028310725'
my_phone_number = '+12026044570'

webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')

free_food = [s for s in soup.body.stripped_strings if 'free' in s.lower()]

body = 'Free Postmates!\n\n' + '\n'.join(free_food)
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12026044570",
    from_="+12028310725",
    body=body
)

print(message.sid)

