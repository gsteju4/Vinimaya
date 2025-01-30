@echo off
:: Navigate to project directory
cd /d D:\Selenium3

::setup a virtual environment
python -m venv venv
call venv\Scripts\activate

::install dependencies
pip install -r requirements.txt

::run python scripts
python Practice.py