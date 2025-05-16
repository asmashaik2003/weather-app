

import requests
from django.shortcuts import render

API_KEY = 'ab5f2413c3ef4b88106e982360f0843a'

def home(request):
    weather_data = None
    error_message = ""

    if request.method == 'POST':
        city = request.POST.get('city')
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            icon_code = data['weather'][0]['icon']
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind'].get('speed', 'N/A'),
                'icon_url': f"http://openweathermap.org/img/wn/{icon_code}@2x.png",
                'main': data['weather'][0]['main'].lower()
            }

        except requests.exceptions.RequestException:
            error_message = "Could not fetch weather data. Please try again."

    return render(request, 'weather.html', {
        'weather': weather_data,
        'error': error_message
    })

