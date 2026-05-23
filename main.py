import requests

api_key = "18b327567f4188aeca8833d6e940ffc6"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"#f stands for fomatted string.

print(url)#shows the whoole data

response = requests.get(url)#data is in json fomat

data = response.json()#converst into python data type 
print(data)
print("\nWeather Report")
print("-------------------")
print("City:", data["name"])
print("Temperature:", data["main"]["temp"], "°C")#accessing nested json.
print("Humidity:", data["main"]["humidity"], "%")#accessing nested json
print("Weather:", data["weather"][0]["description"])