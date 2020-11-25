# from sendEmail import sendEmail
from util import scrape
import urllib3
import json
import datetime

# open file
f = open("links.json", "r")
contents = f.read()
parsedContent = json.loads(contents)

for link in parsedContent:
    http = urllib3.PoolManager()
    page = http.request("GET", link['link'])
    print("Scraping for {}".format(link['name']))
    scrape(page, link['name'], float(link['lowerBound']), float(link['upperBound']))


