from bs4 import BeautifulSoup
from sendEmail import sendEmail
import urllib3
import json

# open file
f = open("links.json", "r")
contents = f.read()
parsedContent = json.loads(contents)

def scrape(page, name, lowerBound, upperBound):
    soup = BeautifulSoup(page.data, 'html.parser')
    results = soup.findAll("td", {"align": "left"})
    for result in results:
        if result.findChildren("a"):
            anchorTag = result.findChildren("a")[0]
            price = anchorTag.find(text=True)[1:]
            try:
                price = float(price)
                if price >= lowerBound and price <= upperBound:
                    link = "http://www.staticice.com.au" + anchorTag['href']
                    print(link)
                    sendEmail(name, price, link)
            except Exception as e:
                print(e)

for link in parsedContent:
    http = urllib3.PoolManager()
    page = http.request("GET", link['link'])
    print("Scraping for {}".format(link['name']))
    scrape(page, link['name'], float(link['lowerBound']), float(link['upperBound']))


