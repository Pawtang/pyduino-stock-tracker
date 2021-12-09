import requests, time, json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np



apikey = "02899e9f7e0ae7f2d2303f1a20a3f45b"
url = "http://api.openweathermap.org/data/2.5/weather?"

q = "chicago"
appid = "GME"
units = "imperial"

# response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def animate(i, xs, ys):
    response = requests.get(f"{url}q={q}&units={units}&appid={apikey}")
    obj = response.json()
    temp = obj["main"]["temp"]
    text = json.dumps(obj, sort_keys=True, indent=4)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Current temperature in Chicago at {current_time}: {temp}")
    xs.append(current_time)
    ys.append(temp)
    xs = xs[-20:]
    ys = ys[-20:]
    ax.clear()
    ax.scatter(xs, ys)
    # plt.draw()
    # time.sleep(2)

ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=300000)
plt.show()