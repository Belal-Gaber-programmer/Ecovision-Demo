import pyttsx3
import speech_recognition as sr
from datetime import datetime
import openai
import requests
import json

openai.api_key = "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"

# Set the correct password for your assistant
password = "Gr33nW0rld$!"

for i in range(3):
    # Prompt the user to enter their password
    user_password = input("Enter the password: ")
    # Verify the entered password
    if user_password == password:
        print("Access granted.")
        break
    elif (i == 2 and user_password != password):
        exit()
    elif (user_password != password):
        print("Try again")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 150)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

bot_name = "Ecovision gpt python voice assistant"
user_name = input("Please enter your name here: ")


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    current_time = datetime.now().time()
    morning_start = datetime.strptime("06:00:00", "%H:%M:%S").time()
    afternoon_start = datetime.strptime("12:00:00", "%H:%M:%S").time()
    evening_start = datetime.strptime("17:00:00", "%H:%M:%S").time()
    night_start = datetime.strptime("21:00:00", "%H:%M:%S").time()

    if morning_start <= current_time < afternoon_start:
        speak("Good morning " + user_name)
    elif afternoon_start <= current_time < evening_start:
        speak("Good afternoon " + user_name)
    elif evening_start <= current_time < night_start:
        speak("Good evening " + user_name)
    else:
        speak("Good night " + user_name)
    speak("I'm Ecovision GPT voice assistant, How can I help you?")


def calculate_transportation_emissions():
    # Emissions from driving
    miles_driven = input(
        "Please enter here how many miles driven to calculate: ")
    miles_driven = int(miles_driven)
    emissions_from_driving = miles_driven * 0.27  # kg CO2 per mile

    # Emissions from flying
    flights_taken = input(
        "Please enter here how many flights taken to calculate: ")
    flights_taken = int(flights_taken)
    emissions_from_flying = flights_taken * 1100  # kg CO2 per flight

    # Total emissions
    total_emissions = emissions_from_driving + emissions_from_flying

    print(total_emissions)


def calculate_energy_emissions():
    # Emissions from electricity usage
    electricity_usage = input(
        "Please enter here how much electricity usage (Kwh) to calculate: ")
    electricity_usage = int(electricity_usage)
    emissions_from_electricity = electricity_usage * 0.5  # kg CO2 per kWh

    # Emissions from natural gas usage
    natural_gas_usage = input(
        "Please enter here how much natural gas usage (therm) to calculate: ")
    natural_gas_usage = int(natural_gas_usage)
    emissions_from_natural_gas = natural_gas_usage * 53.06  # kg CO2 per therm

    # Total emissions
    total_emissions = emissions_from_electricity + emissions_from_natural_gas

    print(total_emissions)


def calculate_food_emissions():
    # Emissions from meat consumption
    meat_consumed = input(
        "Please enter here how much meat consumed (Kg) to calculate: ")
    meat_consumed = int(meat_consumed)
    emissions_from_meat = meat_consumed * 27.3  # kg CO2 per kg of meat

    # Emissions from dairy consumption
    dairy_consumed = input(
        "Please enter how much dairy consumed (Kg) to calculate: ")
    emissions_from_dairy = dairy_consumed * 13.5  # kg CO2 per kg of dairy

    # Total emissions
    total_emissions = emissions_from_meat + emissions_from_dairy

    print(total_emissions)


def recycle_center():
    user_location = input("Enter your location (Postal code, Country): ")
    API_KEY = "d5be75d4dd04476ea4ee5b7d89193f31"
    API_ENDPOINT = "https://api.opencagedata.com/geocode/v1/json?"
    location = user_location.replace(" ", "+")
    url = API_ENDPOINT + "q=" + location + "&key=" + API_KEY
    response = requests.get(url)
    data = json.loads(response.text)
    latitude = data["results"][0]["geometry"]["lat"]
    longitude = data["results"][0]["geometry"]["lng"]
    location = str(latitude) + "," + str(longitude)
    API_ENDPOINT = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    type = "recycling+center"
    radius = 10000  # 10km
    url = API_ENDPOINT + "location=" + location + "&radius=" + \
        str(radius) + "&type=" + type + "&key=" + API_KEY
    response = requests.get(url)
    data = json.loads(response.text)
    results = data["results"]
    if not results:
        speak("No recycling center was found near your location")
    else:
        nearest_recycling_center = results[0]["name"]
        speak("The nearest recycling center to your location is " +
              nearest_recycling_center)


def TaskExe():

    command = sr.Recognizer()
    with sr.Microphone() as mic:
        while True:
            print("listening...")
            command.adjust_for_ambient_noise(mic)
            command.pause_threshold = 1
            audio = command.listen(mic)
            try:
                print("Recognizing...")
                query = command.recognize_google(audio, language='en-us')
                print(f"you said: {query}")
            except:
                speak("sorry, can you say that again")
                continue

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=query,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            response_str = response["choices"][0]["text"].replace("\n", "")
            response_str = response_str.split(
                user_name + ":", 1)[0].split(bot_name + ":", 1)[0]

            print(response_str)

            engine.say(response_str)
            engine.runAndWait()

            if "calculate transportation emissions" in query or "transportation emissions" in query:
                calculate_transportation_emissions()

            elif "calculate energy emissions" in query or "energy emissions" in query:
                calculate_energy_emissions()

            elif "calculate food emissions" in query or "food emissions" in query:
                calculate_food_emissions()

            elif "the nearest recycling centr" in query or "recycling centr" in query or "recycle centr" in query or "the nearest recycling centre" in query or "recycling centre" in query or "recycle centre" in query:
                recycle_center()


wish()
