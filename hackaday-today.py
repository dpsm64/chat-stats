import requests
import re
import datetime
import json
from datetime import date

today = date.today()
month = today.strftime("%m")
day = today.strftime("%d")
years = ['2015','2016','2017','2018','2019','2020']
for year in years:

    url = 'https://hackaday.com/wp-json/wp/v2/posts?author=60022991&status=publish&before=' + year + '-' + month + '-' + day + 'T23:59:59&after=' + year + '-' + month + '-' + day + 'T00:00:00'
    response = requests.get(url)
    posts = json.loads(response.text)
    for post in posts:
        slug = post["slug"]
        link = post["link"]
        title = post["title"]
        filename = "/home/dpm/Documents/hackaday_archives/" + year + "/" + year + month + day + "_" + slug + '.html'
        f = open(filename, "a")
        out = '<h1><a href="' + link + '">' + title["rendered"] + "</a></h1>"
        out = out + "by Dan Maloney                     " + post["date"] 
        content = post["content"]
        out = out + content["rendered"]
        f.write(out)
        f.close()