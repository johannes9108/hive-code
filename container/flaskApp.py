from datetime import datetime, timedelta
from math import e
import stat
from turtle import st
from flask import Flask
from requests import get
import aiohttp
from app import readProjectVersion 
import json
app = Flask(__name__)


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status = response.status
            data = await response.json()
            return status, data
# API Client


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/version")
def version():
    currentVersion = str(readProjectVersion())
    return f"<p>Current version is {currentVersion}</p>"
@app.route("/temperature")
async def temperature():
    currentTime = datetime.now()
    oneHourBefore = currentTime - timedelta(hours=2)
    currentTimeStr = currentTime.isoformat(timespec='seconds') + 'Z'
    oneHourBeforeStr = oneHourBefore.isoformat(timespec='seconds') + 'Z'
    print(oneHourBeforeStr)
    print(currentTimeStr)
    # 2024-10-28T13:45:00Z
    REQUEST =f"https://api.opensensemap.org/boxes?date={oneHourBeforeStr},{currentTimeStr}&phenomenon=temperature"
    status, data = await fetch(REQUEST)
    # Parse the JSON data
    # try:
    #     with open('data-sample.json', 'r') as file:
    #         data = file.read().strip()
    # except Exception:
    #     print("Error reading version file")
    print(status, data[0])
    if not data:
        return "<p>No data found</p>"
    else:
        jsonData = data[0]
        print(jsonData.get('sensors', []))
        # List to collect the values
        temperature_values = []

        # Traverse the JSON structure
        for item in jsonData.get("sensors", []):
            if item.get("title", "").lower() in ["temperature", "temperatur"]:
                print("Found temperature sensor")
                if item.get("lastMeasurement", {}).get("value") is not None:
                    temperature_values.append(float(item.get("lastMeasurement", {}).get("value")))

        # Print the collected values
        print(temperature_values)
        average = sum(temperature_values) / len(temperature_values)
        
        return f"<p>Values measured: {temperature_values}</p><p>Average: {average}</p>"

    