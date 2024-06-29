import requests

# r = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5649f53714ed49fb91ddb69fa7ffe168')
# content = r.json()


def get_news(country, category, api_key='5649f53714ed49fb91ddb69fa7ffe168'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"Title: {article['title']}\nDescription: {article['description']}\n")
    return results

print(get_news('us', 'business'))
