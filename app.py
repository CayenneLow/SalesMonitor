from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.staticice.com.au/cgi-bin/search.cgi?q=sony%20wh-1000xm3&spos=6")

soup = BeautifulSoup(page.content, 'html.parser')
