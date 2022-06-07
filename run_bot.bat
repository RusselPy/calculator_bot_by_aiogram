@echo off

call %~dp0venv\Scripts\activate

cd %~dp0Calculator_Bot

set TOKEN=5074806473:AAF33QF4QNKljbBd4-aZ2xqRfSpJsVdUTvI

python telegram_bot.py

pause