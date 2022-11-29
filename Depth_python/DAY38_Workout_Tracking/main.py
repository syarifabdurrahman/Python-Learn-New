import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load Key
load_dotenv('Depth_python\DAY38_Workout_Tracking\.env')
nutrition_key = os.getenv('NUTRITIONIX_KEY')
nutrition_id = os.getenv('NUTRITIONIX_APP_ID')
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# gender_input = input('Your gender? male or female: ')
exercise_input = input('Tell me which exercise you did: ')


query = exercise_input
gender = 'male'
weight = 80
height = 173
age = 23

data_body = {
    'query': query,
    'gender': gender,
    'weight_kg': weight,
    'height_cm': height,
    'age': age,
}

header = {
    'x-app-id': nutrition_id,
    'x-app-key': nutrition_key
}

response = requests.post(url=exercise_endpoint, headers=header, json=data_body)

data = response.json()

exercise_input = data['exercises'][0]['name']
exercise_time = data['exercises'][0]['duration_min']
exercise_calories = data['exercises'][0]['nf_calories']


sheety_endpoint = 'https://api.sheety.co/9562493db98ab6f8b6b4abcd0949e5bf/workoutsTracking/workouts'

# Adding Row
now = datetime.now()
date_now = now.strftime('%d/%m/%y')
time_now = now.strftime('%H:%M:%S')

workout_body = {
    'workout': {
        "date": date_now,
        "time": time_now,
        "exercise": exercise_input,
        "duration": exercise_time,
        "calories": exercise_calories,
    }
}

basic_header = {
    'Authorization': 'Basic c3lhcmlmOnN5YXJpZjE='
}

response = requests.post(
    url=sheety_endpoint, auth=('syarif', 'syarif1'), headers=basic_header, json=workout_body)
print(response.text)

# # Getting From Sheety
# response = requests.get(sheety_endpoint)
# print(response.text)
