from dotenv import load_dotenv
import os
import requests
import pandas as pd

load_dotenv()
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
def get_location(lat, lng):
    params = {
        'latlng': f'{lat},{lng}',
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None