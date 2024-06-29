import requests

def get_weather(city, units='metric', api_key='e7a47af373f35cc61f2581b0ec3786f0'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open('data.txt', 'a') as file:
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

print(get_weather(city='Washington'))