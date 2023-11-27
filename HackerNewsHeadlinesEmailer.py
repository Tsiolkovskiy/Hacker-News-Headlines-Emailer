import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart

import datetime

now = datetime.datetime.now()

content = ''
def extract_news(url):
    print('Extracting news...')
    cnt = ''
    cnt += ('<b> HN Top Stories: </b> \n'+ '-'*50+'<br>')
    response =requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign': ''})):
        cnt += ((str(i+1)+ ' :: ' +tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        
