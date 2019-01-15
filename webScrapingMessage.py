from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

url = 'https://afesl007.github.io/'
# Your Account SID from twilio.com/console
account_sid = "######################"
# Your Auth Token from twilio.com/console
auth_token  = "########################"

twilio_phone_number = '##########'
my_phone_number = '###########'

# This function attempts to get the content from the url.
# To do this it makes a HTTP request.
# It it is HTMl content then it returns this content.
def get_content(url):
	# try means that it tries something and if it does not work 
	# then it will print out the exception
	try:
		with closing(get(url,stream=True)) as response:
			if response_valid(response):
				return response.content
			else:
				return None
				
	except RequestException as e:
		error_log('There was en error during the web request'.format(url, str(e)))
		return None


# this is a function which controlls if the website is valid. i copied 
# this code from the internet.
def response_valid(response):


    # Returns True if the response seems to be HTML, False otherwise.

	content_type = response.headers['Content-Type'].lower()
	return(response.status_code == 200 and content_type is not None and content_type.find('html') > -1)


# this function only prints the error
def error_log(e):
	print(e)
	
def html_file(content):
	f = open("data.html","w+")
	f.write(str(content))
	f.close



def get_names():
	
	
htmlContent = get_content('https://ai.google/')
html_file(htmlContent)

raw_html = open('data.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('nav'):
	if p['id'] == 'header__nav':
		print(p.text)



webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, 'html.parser')

free_food = [s for s in soup.body.stripped_strings if 'free' in s.lower()]

body = 'Free Postmates!\n\n' + '\n'.join(free_food)
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="##########",
    from_="#############",
    body=body
)

print(message.sid)

