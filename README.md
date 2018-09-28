# CunadoBot

Bot that posts random cunado-like quotes to a Slack channel.
Quotes come from a Google Drive spreadsheet.

# System requirements
```
make
python 3.6
virtualenv
```

## Install
```
make install
```

## Make commands
`make test` will do an isort check and flake8.
`make isort` wil sort the imports.
`make lint` will run flake8.
`make requirements` will generate a new requirements.txt file with the last requirements version.
`make clean` will clean the project folder from unnecessary files.
