from bs4 import BeautifulSoup
from sendEmail import sendEmail
import urllib3
import json

# open file
f = open("links.json", "r")
contents = f.read()
parsedContent = json.loads(contents)

def scrape(page, lowerBound, upperBound):
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
                    sendEmail(price, link)
            except Exception as e:
                print(e)

for link in parsedContent:
    http = urllib3.PoolManager()
    page = http.request("GET", link['link'])
    scrape(page, link['lowerBound'], link['upperBound'])


