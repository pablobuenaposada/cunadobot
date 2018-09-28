import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json, requests
import random
import datetime

SLACK_URL = 'https://hooks.slack.com/services/666'
# change this for testing pourposes
CHANNEL = '#your_channel'

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Desktop/cunao_credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Cunadobot").sheet1
phrases = sheet.get_all_records()


class Cunao(object):	

	@classmethod
	def send_phrase(self):
		day_of_the_year = datetime.datetime.now().timetuple().tm_yday
		selected_phrase = day_of_the_year % (len(phrases))
		text = phrases[selected_phrase]['Phrase']
		data = {
			'channel': CHANNEL,
			'username': 'cunadobot',
			'text': text.upper()
		}
		print(day_of_the_year, selected_phrase, len(phrases), text)
        	requests.post(SLACK_URL, json=data)

Cunao.send_phrase()

