# weather-app
# Django Weather App

A simple and attractive weather application built with Django that fetches real-time weather data using the OpenWeatherMap API.  
Enter any city name to get the current weather, temperature, humidity, and wind speed displayed in a clean and modern interface.

---

## Features

- Fetches live weather data from OpenWeatherMap API  
- Clean and responsive UI with light and dark mode  
- Error handling for invalid city names or API errors  
- Easy to extend and customize  

---

## Tech Stack

- Python 3.x  
- Django Web Framework  
- OpenWeatherMap API  
- HTML, CSS (with modern styling and animations)  
- JavaScript for UI enhancements  

---

## Getting Started

### Prerequisites

- Python 3 installed  
- Django installed (`pip install django`)  
- Requests library (`pip install requests`)  
- An OpenWeatherMap API key (free signup at https://openweathermap.org/api)  

### Installation

1. Clone or download this repository.  
2. In the project directory, open `settings.py` and add your OpenWeatherMap API key.  
3. Run migrations:

```bash
python manage.py migrate
