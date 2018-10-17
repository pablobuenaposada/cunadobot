import json
import os
import random

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

import settings

USED_PHRASE_FILE = 'used_phrases.json'
USED_PHRASE_KEY = 'used_phrases'
SLACK_URL = settings.SLACK_URL
# change this for testing pourposes
CHANNEL = settings.SLACK_CHANNEL


def get_phrases():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        settings.CREDENTIALS_FILE,
        scope)
    client = gspread.authorize(creds)

    sheet = client.open(settings.SHEET_NAME).sheet1
    return sheet.get_all_records()


def get_used_phrases():
    """Read the USED_PHRASE_FILE file and return a set with all the indexs
    of the used phrases.

    Returns:
        set(int): Set with the index of the phrases
    """
    used_phrases = set()
    try:
        with open(USED_PHRASE_FILE) as json_file:
            used_phrases = json.load(json_file)
    except Exception:
        pass

    if used_phrases and USED_PHRASE_KEY in used_phrases.keys():
        used_phrases = set(used_phrases[USED_PHRASE_KEY])

    return used_phrases


def reset_used_phrase_file():
    os.remove(USED_PHRASE_FILE)


def choice_phrase(amount_phrases, used_phrases):
    all_phrases = set(range(amount_phrases))
    not_used_phrases = list(all_phrases - used_phrases)

    if not_used_phrases:
        return random.choice(not_used_phrases)

    reset_used_phrase_file()
    return random.choice(list(all_phrases))


def add_used_phrase_idx(used_phrases_idx, phrase_idx, phrases_amount):
    if phrases_amount <= len(used_phrases_idx):
        used_phrases_idx = []
    used_phrases_idx.append(phrase_idx)
    data = {USED_PHRASE_KEY: used_phrases_idx}
    with open(USED_PHRASE_FILE, 'w+') as file:
        file.write(json.dumps(data))


def main():
    phrases = get_phrases()
    phrases_amount = len(phrases)
    used_phrases = get_used_phrases()
    selected_phrase = choice_phrase(phrases_amount, used_phrases)

    text = phrases[selected_phrase]['Quote']
    data = {
        'channel': CHANNEL,
        'username': 'cunadobot',
        'text': text.upper()
    }
    # print(selected_phrase, phrases_amount, text)
    requests.post(SLACK_URL, json=data)

    add_used_phrase_idx(list(used_phrases), selected_phrase, phrases_amount)


if __name__ == '__main__':
    main()
