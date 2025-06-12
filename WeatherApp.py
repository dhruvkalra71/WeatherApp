import requests

print("Welcome to Weather App!")
city_name = input("Enter city name: ") # Prompt to Enter city name
API_key = '' # Enter your API key here

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    #print(data)
    print("City Name = ", data['name'])

    print(f'Longitude = {data['coord']['lon']} and Latitude = {data['coord']['lat']}')
    print(f'Weather is {data['weather'][0]['main']}')
    print(f'Temperature = {data['main']['temp']}')
    print(f'Feels like {data['main']['feels_like']}')
    print(f'Temperature Minimum = {data['main']['temp_min']}')
    print(f'Temperature Maximum = {data['main']['temp_max']}')
    print(f'Pressure = {data['main']['pressure']}')
    print(f'Humidity = {data['main']['humidity']}')
    print(f'Sea_level = {data['main']['sea_level']}')
    print(f'Ground Level = {data['main']['grnd_level']}')
    print(f'Visibility = {data['visibility']}')

else:
    print("Error 404")
