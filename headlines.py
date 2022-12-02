"""
Stage : Development -01
@author : Yiğit Nihat Doğancık , 120200084
@author : Lütfü Orçun Selbasan , 119200063
@author : Sinan Hacisoyu, 119200060

"""

from bs4 import BeautifulSoup
import requests
#alternative to request

#file = codecs.open("science.html", "r", "utf-8")
#soup = BeautifulSoup(file, 'html.parser')

#print(file.read())

nytimes_sciences = "https://www.nytimes.com/section/science"
res = requests.get(nytimes_sciences)
soup = BeautifulSoup(res.content, 'html.parser')

headers = soup.select("li.css-112uytv div div a h2")
#dates = soup.select("li.css-112uytv div.css-1cp3ece div.css-agsgss span")
#print(dates)
for header in headers:
    print(header.text)

#we may get date information using urls in the link tags.
dates = soup.select("li.css-112uytv div.css-1cp3ece div.css-agsgss span")
print(dates)