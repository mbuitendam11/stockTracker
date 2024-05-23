import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

## AlphaVantage API Key
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_API_KEY = ""

## Newsapi API Key
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ""


## GET stock prices
stockParameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY,
    "outputsize": "compact"
}

stockResponse = requests.get(url=STOCK_ENDPOINT, params=stockParameters)
stockResponse.raise_for_status()
data = stockResponse.json()["Time Series (Daily)"]
dataList = [value for (key, value) in data.items()]

## GET News
newsParams = {
    "apikey": NEWS_API_KEY,
    "q": COMPANY_NAME,
}

newsResponse = requests.get(url=NEWS_ENDPOINT, params=newsParams)
newsResponse.raise_for_status()
newsData = newsResponse.json()["articles"][:3]

newsList = [f"Headline: {article['title']}. \nBrief: {article['description']}. \nurl:{article['url']}" for article in newsData]
body = "\r\n\n".join(newsList)

    ## Run the print

## GET Previous Closing Data
previous_data = dataList[1]["4. close"]

## GET Yesterday Day Closing Data
yesterday_data = dataList[0]["4. close"]

diff = abs(float(yesterday_data) - float(previous_data))
percentageDiff = abs(float(yesterday_data) / float(previous_data) * 100)

if percentageDiff > 100:
    remain = abs(percentageDiff - 100)
    print(f"{STOCK_NAME} closed up {remain}\n")
    print(f"{STOCK_NAME} closed at {yesterday_data}")
    print(body)
elif percentageDiff == 100:
    print(f"No Change, remains at {previous_data}\n")
    print(f"{STOCK_NAME} closed at {yesterday_data}")
    print(body)
elif percentageDiff < 100:
    remain = abs(percentageDiff - 100)
    print(f"{STOCK_NAME} closed down {remain}\n")
    print(f"{STOCK_NAME} closed at {yesterday_data}")
    print(body)


