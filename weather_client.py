
import requests
import logging

def get_weather_data(api_key: str, city_name: str):
    """
    Creating a function that gets the weather data of the city name using the generated api key
    Website used:OpenWeatherMap
    Constructed URL makes get request to OpenWeather API
    :param api_key: 
    :param city_name: 
    :return: Weather data for a particular city in JSON response
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return f"Weather data retrieved: \n {response.json()}  "
        else:
            return f"Not retrieved, {response.status_code}"
    except Exception:
        raise Exception("Retrieval of weather data failed")

def convert_to_celcius(kelvin_degree: float):
    """
    Function converts temperature in kelvin to celcius
    :param kelvin_degree:
    :return: Temperature in celcius
    """
    try:
        return round(kelvin_degree-272.15, 2)
    except Exception:
        raise Exception("Invalid conversion")

def display_weather_info(api_key: str, city_name: str):
    """
    Display all weather information of the city:
    Display weather temperature converted to a celcius
    Display humidity level of the city
    Display wind speed measured in m/s
    Display weathter description

    :param api_key:
    :param city_name:
    :return:weather info for a city
    """
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200: #staus code 200 is successful
            weather_data = response.json()

            weather_temp = weather_data["main"]["temp"] # display temp

            humidity_level = weather_data["main"]["humidity"] #display humid level

            wind_speed = weather_data["wind"]["speed"] # display wind speed

            weather_descrp = weather_data["weather"][0]["description"] # display weather descrp

            print(f"Weather temperature for {city_name}: {convert_to_celcius(weather_temp)}")

            print(f"Weather description for {city_name}: {weather_descrp}")

            print(f"Humidity level of {city_name}: {humidity_level}")

            print(f"Wind speed of {city_name}: {wind_speed}")

        elif response.status_code == 404:
            print(f"City not found")

        elif response.status_code == 401:
            print(f"Invalid api key")

    except requests.exceptions.ConnectionError:
        return "Connection error, please check internet connection"

    except requests.exceptions.Timeout:
        return "Request timed out"

    except requests.exceptions.RequestException as e:
        return f"An error occured:{e}"


def main():
    """
    Main function that prompts user to enter the name of city
    :return: weather info for the city
    """

    apikey = "a8c314cd32cb8689779878490c54845d"
    cityname = input("Enter name of city: ")

    display_weather_info(apikey, cityname)


if __name__ == "__main__":
    main()


# print(main())
# print(convert_to_celcius(272.15))
# print(get_weather_data("a8c314cd32cb8689779878490c54845d", "London"))