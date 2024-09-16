import unittest
from unittest.mock import patch, Mock
from weather_client import display_weather_info, convert_to_celcius
from io import StringIO


class TestWeatherClient(unittest.TestCase):
    def test_convert_celcius(self):
        """
        Test conversion function of kelvin to celcius;
        to confirm accurate conversions
        """
        self.assertEqual(0.0, convert_to_celcius(272.15))


    def test_successful_response(self, mock_get):
        """
        Testing for successful api request response with sample weather data;
        using patch as context manager to mock requests for the sample weather data

        :param mock_get:
        :return:
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "name": "London",
            "main": {
                "temp": 15,
                "humidity": 60,
            },
            "weather": [
                {"description": "broken clouds"}
            ],
            "wind": {
                "speed": 3.76
            }
        }
        mock_get.return_value = mock_response

        with patch("sys.stdout", new=StringIO()) as fake_out: #replace console output with StringIO obj
            display_weather_info("dummy_api_key", "London")
            output = fake_out.getvalue() #capture output

        self.assertIn("Weather temperature for London: -257.15", output)
        self.assertIn("Weather description for London: broken clouds", output)
        self.assertIn("Humidity level of London: 60", output)
        self.assertIn("Wind speed of London: 3.76", output)


    def test_city_not_found(self, mock_get):
        """
        Test for error status code 404 - City not found
        Mock 404 response for city not found
        :param mock_get:
        :return:
        """
        mock_get.return_value.status_code = 404

        with patch('sys.stdout', new=StringIO()) as fake_out:
            display_weather_info("InvalidCity", "valid_api_key")
            output = fake_out.getvalue()

        self.assertIn(f"City not found", output) # Output must contain "city not found" message


    def test_invalid_apikey(self, mock_get):
        """
        Test for invalid api key- 401 response
        :param mock_get:
        :return:
        """
        mock_get.return_value.status_code = 401

        with patch("sys.stdout", new=StringIO()) as fake_out: #pinted output captured
            display_weather_info("London", "Invalid api key")
            output = fake_out.getvalue()

        self.assertIn(f"Invalid api key", output) #Output must contain iinvalid api key message


if __name__ == "__main__":
    unittest.main()



