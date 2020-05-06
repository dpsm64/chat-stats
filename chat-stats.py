# chat-stats.py (c) 2020 Daniel P. Maloney
# scrape Hack Chat attendance stats and display
import requests
import re
import datetime
from bs4 import BeautifulSoup
url="https://hackaday.io/messages/room/2369"
page = requests.get(url)
patt_mem = re.compile('(?P<members>\d+)/\d+ Members, (?P<anonymous>\d+) Anonymous')
now = datetime.datetime.now()

soup = BeautifulSoup(page.content, 'html.parser')
results= soup.find(id="chat")
member_elems = results.find_all('h3', class_="members-title")
if len(member_elems) > 0:    
    m = patt_mem.search(member_elems[0].text)
    mem = int(m.group('members'))
    anon = int(m.group('anonymous'))
    total = mem + anon
    print(now.strftime("%Y-%m-%d %H:%M:%S"), '\t', mem, '\t', anon, '\t', total)
else:
    print(now.strftime("%Y-%m-%d %H:%M:%S") , '\t', "Timeout")