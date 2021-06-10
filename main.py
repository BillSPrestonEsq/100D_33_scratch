import requests

MY_LAT = 38.785809
MY_LONG = -77.187248

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response.json())

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()

print(response2.json())

sunrise = response2.json()["results"]["sunrise"]
sunset = response2.json()["results"]["sunset"]

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

print(f"{sunrise_hour}, {sunset_hour}")