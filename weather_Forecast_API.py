import requests

def get_weather(city_name, units='metric', api_key='d8a1da28f652528b32e2055e0b6859c5'):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={units}"
    r = requests.get(url)
    content = r.json()
    city_name = content['city']['name']

    with open('data.txt', 'a') as file:

        for item in content['list']:
            file.write(f"{city_name}, {item['dt_txt']}, {item['main']['temp']}, {item['weather'][0]['description']}\n")
            # print(city_name, item['dt_txt'], item['main']['temp'], item['weather'][0]['description'])

print(get_weather(city_name='ecatepec'))


