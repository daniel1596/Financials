@echo off

:: pip install -r docs/requirements.txt
python app.py --init_db

echo Installation complete.
echo.
:: Additional future tasks for this file would include:
:: - Calling a (Python?) script to clear all transaction data from the db (just in case), etc.
:: - Maybe some sort of readme popping up on the screen? Not sure if that would be needed.

:: (Note - don't need to install npm. Vue is included via script reference.)


pause