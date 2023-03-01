from datetime import datetime
import re
import urllib.request

city = input("Введите город: ",)

city_pattern = r'(?:name":")([^"]+)'
temp_pattern = r'(?:temp":)([^,]+)'
desc_pattern = r'(?:description":")([^"]+)'
humid_pattern = r'(?:humidity":)([^,}]+)'
speed_pattern = r'(?:speed":)([^,]+)'
pressure_pattern = r'(?:pressure":)([^,]+)'

response = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f").read().decode()

match_city = re.findall(city_pattern, response)
match_temp = re.findall(temp_pattern, response)
match_desc = re.findall(desc_pattern, response)
match_humid = re.findall(humid_pattern, response)
match_speed = re.findall(speed_pattern, response)
match_pressure = re.findall(pressure_pattern, response)

print(match_city, match_temp, match_desc, match_humid, match_speed, match_pressure)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"[{current_time}] Запрос погоды в городе: {match_city}"
      f"Температура: {(match_temp)}")
