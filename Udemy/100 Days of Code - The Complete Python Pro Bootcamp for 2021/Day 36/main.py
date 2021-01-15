import requests
import datetime


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = 'STOCK_API'
NEWS_API_KEY = 'NEWS_API'

stock_url = 'https://www.alphavantage.co/query'
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_url = 'http://newsapi.org/v2/everything'
news_parameters = {
    "q": COMPANY_NAME,
    "sortBy": 'publishedAt',
    "apiKey": NEWS_API_KEY,
}


request = requests.get(url=stock_url, params=stock_parameters).json()["Time Series (Daily)"]

yesterday_close = float(request[list(request.keys())[0]]["4. close"])
previous_close = float(request[list(request.keys())[2]]["4. close"])

if abs(yesterday_close/previous_close - 1) > 0.05:
    news =  requests.get(url=news_url, params=news_parameters).json()["articles"][:3]
    news = [paper["source"]["name"]+": "+paper["title"]  for paper in news]

