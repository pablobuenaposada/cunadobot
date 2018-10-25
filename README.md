# CunadoBot

[![Build Status](https://travis-ci.org/pablobuenaposada/cunadobot.svg?branch=master)](https://travis-ci.org/pablobuenaposada/cunadobot)

Bot that posts random cunado-like quotes to a Slack channel.
Quotes come from a Google Drive spreadsheet.

## System requirements
```bash
make
python 3.6
virtualenv
```

## Install
Run `make install` and modify settings.py with your sensitive data.

Then add this bot to cron so it's triggered every work day at 12:00 PM for example (replace the cunadobot folder):
```sh
crontab 00 12 * * mon-fri cd cunadobot-folder/ && make run
```
## Quotes source
Quotes will be picked from a Google Drive spreadsheet, for testing purposes settings.example.py is set to use [this](https://docs.google.com/spreadsheets/d/1Op02wAow7MEStkCtzAoNhDcbr6osR2AJAUdlIkFZ_yk/edit?usp=sharing) public one.

Use the same template to make your own.

## Make commands
  - `make test` will do an isort check and flake8.
  - `make isort` wil sort the imports.
  - `make lint` will run flake8.
  - `make requirements` will generate a new requirements.txt file with the last requirements version.
  - `make clean` will clean the project folder from unnecessary files.
  - `make run` will run the cunadobot with the daily quote.
