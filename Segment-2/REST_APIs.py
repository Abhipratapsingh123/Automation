import requests

r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5649f53714ed49fb91ddb69fa7ffe168')
content = r.json()
print(content['articles'][0]['title'])




