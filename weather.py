import requests, time, json



apikey = "02899e9f7e0ae7f2d2303f1a20a3f45b"
url = "http://api.openweathermap.org/data/2.5/weather?"

q = "chicago"
appid = "GME"
units = "imperial"

# response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo")

while True:
    response = requests.get(f"{url}q={q}&units={units}&appid={apikey}")
    obj = response.json()
    temp = obj["main"]["temp"]
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(f"Current temperature in Chicago: {temp}")
    time.sleep(5)