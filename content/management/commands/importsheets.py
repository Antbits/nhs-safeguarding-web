from base64 import encode
import csv
import unicodedata
from django.core.management.base import BaseCommand
from wagtail.core.models import Page, Site
from wagtail.core.fields import RichTextField, StreamField
from content.models import ContactIndexPage, ContactPage
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow,Flow
from google.auth.transport.requests import Request
import os
import pickle
import json

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID_input = '1h7ikTqSOqWjGU2ArhsSwfPoGYoYXxtIPSHjWMF6Iho0'
SAMPLE_RANGE_NAME = 'contact!A2:H'


class Command(BaseCommand):
    help = "Imports GSHEETS"
    #local_path = '/home/dev/nhs_safeguarding/nhs_safeguarding/nhs_safeguarding/'
    local_path = '.'
    indexes = {}
    ContactPage.objects.all().delete()
    ContactIndexPage.objects.all().delete()
    for key in Page.objects.all():
            if key.title == "Contacts":
                home = Page.objects.get(id=key.id)
                print('Contacts found')

    global values_input, service
    def handle(self, *args, **options):
        creds = None
    def sanitize(str):
        return str.replace(" ", "-").replace(",", "").replace("&", "and").lower()
    if os.path.exists('token.pickle'):
        with open(local_path+'/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
               local_path+'/token.json', SCOPES) 
            creds = flow.run_local_server(port=0)
        with open(local_path+'/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result_input = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID_input,
                                range=SAMPLE_RANGE_NAME).execute()
    values_input = result_input.get('values', [])

    if not values_input and not values_expansion:
        print('No data found.')
    df=pd.DataFrame(values_input[0:], columns=[0,1,2,3,4,5])
    # generate index pages
    region = 'null'
    for index, row in df.iterrows():
        if region != row[0]:
            region = row[0]
           
            key = sanitize(row[0])
            contact_index_page = ContactIndexPage(
                slug = key+'-index',
                title=row[0]
            )
            indexes[key] = contact_index_page
   # populate index pages 
    df.reset_index
    region = 'null'
    index_html = ''
    count = 0
    i = 0
    for index, row in df.iterrows():
        i +=1
        subkey = sanitize(row[1])
        
        if region != row[0] and count > 0 or i == len(df):
            if i == len(df):
                index_html += '<li><a href="'+subkey+'"><b>'+row[1]+'</b></a></li>'
            
            index_html += '</ul>'
            indexes[key].content  =json.dumps([
                {'type':'paragraph', 'value': index_html}
            ])
            home.add_child(instance=indexes[key])
        else:
            index_html += '<li><a href="'+subkey+'"><b>'+row[1]+'</b></a></li>'
            
            
        if region != row[0]:
            index_html = '<ul><li><a href="'+subkey+'"><b>'+row[1]+'</b></a></li>'
            count += 1
            region = row[0]
       
        key = sanitize(row[0])
    # generate contact pages
    df.reset_index
    region = 'null'
    index_html = ''
    count = 0
    i = 0
    child_description = ''
    adult_description = ''
    content = ''

    for index, row in df.iterrows():
        i +=1
        if i == 1:
            child_description = row[3]
        if i == 1:
            adult_description = row[5]
        key = sanitize(row[0])
        subkey = sanitize(row[1])

        content = '<ul>'
        if row[2] is not None:
            content += '<li><a href="'+row[2]+'">'+child_description+'</a></li>'
        if row[4] is not None:
            content += '<li><a href="'+row[4]+'">'+adult_description+'</a></li>'
        content += '</ul>'
        contact_page = ContactPage(
            slug = subkey,
            title=row[1],
            content = json.dumps([
                {'type':'paragraph', 'value': content}
            ])
            
         )
        print(subkey)
        indexes[key].add_child(instance=contact_page)
    

            
            
           
            
