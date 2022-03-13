# TimeFromNow Telegram Bot

## Description
TimeFromNowBot was developed for Genshin Impact mobile players to calculate the time required to fully replenish their original resin.
However, this telegram bot can be used for any sort of "time from now" calculations.

| Bot Command | Description |
| --- | --- |
| `/start` | Start TimeFromNowBot |
| `/help` | View Instructional Information |
| `/credits` | View Developer Information |
| `/time` | Display Current Time (24-Hour Format) |

 Note: [PyCharm](https://www.jetbrains.com/pycharm/) (Python IDE) is recommended but not required to run this project.
 Please use the telegram bots commands where applicable.

## Timing Format to Follow

| Bot Usage | Description |
| --- | --- |
| `HH:MM:SS` | `(eg. 01:15:30)` for 1 hour, 15 minutes and 30 seconds |
| `HH:MM:SS` | `(eg. 22:00:00)` for 22 hours, 0 minute and 0 second |

## Legend

| Abbreviations | Usage Examples |
| --- | --- |
| `HH = Hours` | `01` to `24` |
| `MM = Minutes` | `01` to `59` |
| `SS = Seconds` | `01` to `59` |

## Telegram API Key
1. Get a HTTP API Key from BotFather on telegram
2. Enter the newly acquired API Key into api.py
```
API_KEY = 'EnterYourAPIKey'
```

## Required Libraries
- python-telegram-bot

## Installation
```
pip install -r requirements.txt
```
