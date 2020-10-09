# chat-members.py (c) 2020 Daniel P. Maloney
# scrape Hack Chat attendance members
import requests
import re
import datetime
from bs4 import BeautifulSoup
import csv

# set up dict
users = None
now = datetime.datetime.now()
timepoint = now.strftime("%Y-%m-%d %H:%M:%S")
delim = '\t'
tmp = []
# read in URL
url="https://hackaday.io/messages/room/2369"
page = requests.get(url)

# parse 
soup = BeautifulSoup(page.content, 'html.parser')
results= soup.find(id="chat")

if page.status_code == 200:
    chat = results.find(class_="chat-sidebar-section members-list")
    for member in chat.children:
        user = member.find('h4')
        # record online users
        if user is not None and user.previous_sibling.find('span', class_="user-indicator online") is not None:
            #print(user.string)
            tmp.append(user.string)
    users = delim.join(tmp)
    print(delim.join([timepoint,users]))
    
    # write it out to csv file
    #with open('hackchat_users.csv', 'a', newline='', encoding='utf-8') as csv_file:
    #    fields = ['time','users']
    #    writer = csv.DictWriter(csv_file, fieldnames=fields)
    #   writer.writerow(users) 
else:
    print(page.status_code)