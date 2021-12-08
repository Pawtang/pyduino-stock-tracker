import requests, time, json

function = "GLOBAL_QUOTE"
symbol = "GME"
interval = "1min"
apikey = "8FHBY3IH2VNLQYKG"

url = "https://www.alphavantage.co/query?"



# response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo")

while True:
    response = requests.get(f"{url}function={function}&symbol={symbol}&interval={interval}&apikey={apikey}")
    obj = response.json()
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    time.sleep(5)
