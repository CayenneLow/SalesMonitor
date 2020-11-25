from util import scrape
import json
import datetime
import urllib3

http = urllib3.PoolManager()

def lambda_handler(event, context):
    # open file
    f = open("links.json", "r")
    contents = f.read()
    parsedContent = json.loads(contents)

    print("=== Executing now at: {} ===".format(datetime.datetime.now()))
    for link in parsedContent:
        page = http.request("GET", link['link'], timeout=10.0)
        if "blocked" in page:
            print(page)
            raise Exception("Current ip address blocked")
        print("Scraping for {}".format(link['name']))
        scrape(http, page, link['name'], float(link['lowerBound']), float(link['upperBound']))

lambda_handler(None, None)