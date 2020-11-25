# from sendEmail import sendEmail
from util import scrape
import requests
import json
import datetime

def lambda_handler(event, context):
    # open file
    f = open("links.json", "r")
    contents = f.read()
    parsedContent = json.loads(contents)

    print("=== Executing now at: {} ===".format(datetime.datetime.now()))
    for link in parsedContent:
        page = requests.get(link['link'], timeout=10).text  # timeout after 10 seconds
        if "blocked" in page:
            raise Exception("Current ip address blocked")
        print("Scraping for {}".format(link['name']))
        scrape(page, link['name'], float(link['lowerBound']), float(link['upperBound']))


