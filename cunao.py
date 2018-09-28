import datetime

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

import settings

SLACK_URL = settings.SLACK_URL
# change this for testing pourposes
CHANNEL = settings.SLACK_CHANNEL

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    settings.CREDENTIALS_FILE,
    scope)
client = gspread.authorize(creds)

sheet = client.open(settings.SHEET_NAME).sheet1
phrases = sheet.get_all_records()


def main():
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


if __name__ == '__main__':
    main()
