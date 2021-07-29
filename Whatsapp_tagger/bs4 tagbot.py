# this is purely experimental.
# possible consequences, u might end up sending gibberish to ur groups and they might kill you

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://web.whatsapp.com"

try:
   page = urlopen(url)
except:
   print("Error opening the URL")

BeautifulSoup.parse(page, 'html.parser')