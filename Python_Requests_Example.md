# Sample Program to Fetch Price from Amazon and choose to buy if certain criteria is met
```python
__author__ = 'deepakmane'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/Apple-MacBook-Retina-2-8GHz-Quad-core/dp/B07SKPVDFF/ref=sr_1_5?keywords=macbook+pro+1TB&qid=1577338835&sr=8-5")
content = request.content
soup = BeautifulSoup(content, "html.parser")
#<span id="priceblock_ourprice" class="a-size-medium a-color-price priceBlockBuyingPriceString">$2,579.95</span>
element = soup.find("span", {"id": "priceblock_ourprice", "class": "a-size-medium a-color-price priceBlockBuyingPriceString"})
string_price = element.text.strip() # "$2,579.95"
string_price = string_price.replace(',', '')
price_without_symbol = string_price[1:] # "$2,579.95"
price = float(price_without_symbol)

if(price < 2000):
    print("buy the mac book laptop which is {}.".format(string_price))
else:
    print("Wait to buy the mac book laptop which is {}.".format(string_price))
```
