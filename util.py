from bs4 import BeautifulSoup
import urllib3

def scrape(http, page, name, lowerBound, upperBound):
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
                    if (not isOutOfStock(http, getPage(link))):
                        print(link)
                        sendEmail(name, price, link)
            except Exception as e:
                print(e)

def getPage(http, link):
    # Get redirection page
    page = http.request("GET", link['link'], timeout=10.0)
    print(page)
    soup = BeautifulSoup(page.data, 'html.parser')
    metaTag = soup.find("meta")
    redirect = metaTag["content"].split("=")[1]
    # Access redirect page
    html = requests.get(redirect).text
    return html

def isOutOfStock(page):
    page = page.lower()
    keywords = ["Out of Stock", "Notify me", "Pre Order", "Pre-Order", "Sold Out", "Discontinued"]
    for keyword in keywords:
        keyword = keyword.lower()
        if keyword in page:
            return True
    return False