@echo off
:: Navigate to project directory
cd /d D:\POM_Framework

::setup virtual environment
python -m venv venv
call venv\Scripts\activate

::install dependencies
pip install -r requirements.txt

::run python scripts
python Homepage.py
python Login.py
python test_login.py
