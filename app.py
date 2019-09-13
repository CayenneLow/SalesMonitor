from bs4 import BeautifulSoup
from sendEmail import sendEmail
import urllib3

http = urllib3.PoolManager()
page = http.request(
    "GET", "http://www.staticice.com.au/cgi-bin/search.cgi?q=bose+qc35&spos=3")
soup = BeautifulSoup(page.data, 'html.parser')

results = soup.findAll("td", {"align": "left"})
for result in results:
    if result.findChildren("a"):
        anchorTag = result.findChildren("a")[0]
        price = anchorTag.find(text=True)[1:]
        try:
            price = float(price)
            if price >= 200 and price <= 350:
                link = "http://www.staticice.com.au" + anchorTag['href']
                print(link)
                sendEmail(price, link)
        except Exception as e:
            print(e)