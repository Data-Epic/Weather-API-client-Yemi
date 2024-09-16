# Weather Data Client Application  
## Overview   
The Python application interacts with the OpenWeather API to fetch and display weather for any city available. The applioocation prompts users to input  any given city name and displays the folllowing information:  
*City name*  
*Tempearture - Celcius*  
*Weather description*   
*Humidity Level*   
*Wind speed*   
## Features  
1. Fetches real-time weather using OpenWeatherMap API
2. Displays the relevant weeather information for a city  
3. Handles errors such as invalid api keys and unavailable/invalid cities  
4. Pyhon test scripts to validate the appllications   
# Packages/Prerequisites   
1. requests library for requesting weather data api   
2. Python 3.x  
3. OpeanWeatherMap API key  
# Application Usage   
1. Run application in terminal - pythhon weather_client.py   
2. Input City Name- The application prompts you to enter a city name  
3. Dispaly weather information for city: ****Temp, Weather descrp, Humidity level, Wind speed***
## Error Handling   
### The application handles invalid api key and non-existent cities errors   
1. Invalid API key: Provided API key is invalid the appplication outputs the message *"Invalid API key"*  
2. Non-existent city: Provided City name is invalid or not existent in the weather data api, the application outputs a message *"City not found"*
