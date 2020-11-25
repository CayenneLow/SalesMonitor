# from sendEmail import sendEmail
from util import scrape, reboot
import requests
import json
import datetime

# open file
f = open("links.json", "r")
contents = f.read()
parsedContent = json.loads(contents)

print("=== Executing now at: {} ===".format(datetime.datetime.now()))
for link in parsedContent:
    page = requests.get(link['link']).text
    if "blocked" in page:
        # reboot ec2 instance
        reboot()
        return
    print("Scraping for {}".format(link['name']))
    scrape(page, link['name'], float(link['lowerBound']), float(link['upperBound']))


