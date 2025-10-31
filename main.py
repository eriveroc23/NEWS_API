import requests

def get_news(topic, from_date, to_date, language='en', api_key='db94a1853de742fe95588f8e1cf01b0d'):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'qInTitle': topic,
        'from': from_date,
        'to': to_date,
        'sortBy': 'popularity',
        'language': language,
        'apiKey': api_key
    }

    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    content = r.json()
    articles = content.get('articles', []) or []
    results = []
    for article in articles:
        title = article.get('title') or 'No title'
        description = article.get('description') or 'No description'

        results.append(f"Title:\n{title}\nDescription:\n{description}")
    return results


elements = get_news(topic='space', from_date='2025-10-29', to_date='2025-10-30')

for num, element in enumerate(elements):
    print(num+1, element)