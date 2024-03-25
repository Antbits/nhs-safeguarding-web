# NHS Safeguarding Web App

A Wagtail driven web application

# Getting started

Install python & Wagtail, open a terminal in the main directory and activate the venv:

.\venv\Scripts\activate

Create a local mysqlite3 database and perform migrations as per Wagtail instructions here https://docs.wagtail.org/en/stable/getting_started/

Then run Wagtail:

python manage.py runserver

To import Google Sheets data run:

python ./manage.py importsheets

This will only work if there is a page titled "Contacts", the sheets importer will create all contacts as child pages of "Contacts"