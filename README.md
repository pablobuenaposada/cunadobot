# CunadoBot

Bot that posts random cunado-like quotes to a Slack channel.
Quotes come from a Google Drive spreadsheet.

## System requirements
```
make
python 3.6
virtualenv
```

## Install
```
make install
```
you can add this bot to cron so it's triggered every work day at 12:00 PM for example (replace the cunadobot folder):
```sh
crontab 00 12 * * mon-fri cd cunadobot-folder/ && make run
```

## Make commands
- `make test` will do an isort check and flake8.
- `make isort` wil sort the imports.
- `make lint` will run flake8.
- `make requirements` will generate a new requirements.txt file with the last requirements version.
- `make clean` will clean the project folder from unnecessary files.
- `make run` will run the cunadobot with the daily quote.
