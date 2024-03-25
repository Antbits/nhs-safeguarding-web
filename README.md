# NHS Safeguarding Web App

# NHS Safeguarding web application

A Wagtail driven web application

# Getting started

Install Python, Wagtail and Venv

Create a local mysqlite3 database and perform migrations as per Wagtail instructions here https://docs.wagtail.org/en/stable/getting_started/

To import Google Sheets data run:

    > python ./manage.py importsheets

This will only work if there is a page titled "Contacts", the sheets importer will create all contacts as child pages of "Contacts"

Please contact NHS England if you require an archive of the site content