import json
import os
import random

import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials

import settings

USED_QUOTE_FILE = 'used_quotes.json'
USED_QUOTE_KEY = 'used_quotes'


def get_quotes():
    """
    Use creds to create a client to interact with the Google Drive API
    """

    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        settings.CREDENTIALS_FILE,
        scope)
    client = gspread.authorize(creds)

    sheet = client.open(settings.SHEET_NAME).sheet1

    return sheet.get_all_records()


def get_used_quotes():
    """
    Read the USED_QUOTE_FILE file and return a set with all the indexs
    of the used quotes.

    Returns:
        set(int): Set with the index of the quotes
    """

    used_quotes = set()
    with open(USED_QUOTE_FILE) as json_file:
        used_quotes = json.load(json_file)

    if used_quotes and USED_QUOTE_KEY in used_quotes.keys():
        used_quotes = set(used_quotes[USED_QUOTE_KEY])

    return used_quotes


def reset_used_quote_file():
    os.remove(USED_QUOTE_FILE)


def choice_quote(amount_quotes, used_quotes):
    all_quotes = set(range(amount_quotes))
    not_used_quotes = list(all_quotes - used_quotes)

    if not_used_quotes:
        return random.choice(not_used_quotes)

    reset_used_quote_file()

    return random.choice(list(all_quotes))


def write_quote_to_slack(quote):
    """
    Writes the uppercase quote to the selected slack web hook
    """

    for url in settings.SLACK_URLS:
        # TODO: catch post exceptions in order to continue posting with the remaining urls
        requests.post(url, json={'text': quote.upper()})


def add_used_quote_idx(used_quotes_idx, quote_idx, quotes_amount):
    if quotes_amount <= len(used_quotes_idx):
        used_quotes_idx = []
    used_quotes_idx.append(quote_idx)
    data = {USED_QUOTE_KEY: used_quotes_idx}
    with open(USED_QUOTE_FILE, 'w+') as file:
        file.write(json.dumps(data))


def main():
    quotes = get_quotes()
    quotes_amount = len(quotes)
    used_quotes = get_used_quotes()
    selected_quote = choice_quote(quotes_amount, used_quotes)
    quote = quotes[selected_quote]['Quote']

    write_quote_to_slack(quote)

    add_used_quote_idx(list(used_quotes), selected_quote, quotes_amount)
