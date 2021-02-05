import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import lxml

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
}


response = requests.get(url="https://www.amazon.com/Samsung-Factory-Unlocked-Smartphone-Pro-Grade/dp/B08FYVMRM5/",
                        headers=header)
soup = BeautifulSoup(response.text, parser="lxml")
price = soup.select(selector="#priceblock_ourprice")[0].text.split("$")[1]
full_price = int(price.split(".")[0]) + int(price.split(".")[1])/100

