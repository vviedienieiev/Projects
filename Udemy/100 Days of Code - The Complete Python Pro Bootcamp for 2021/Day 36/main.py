import requests
import datetime


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = 'ZBAIXFWGOQD6NZKU'
NEWS_API_KEY = '5bf37da4d716417e852f970eb52d1353'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

