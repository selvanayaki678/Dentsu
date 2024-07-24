#To run the script python extract_data_api.py
import requests
import json

# The API endpoint for fetching the data
input_api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

def extract_api_data(api):
    """
    Fetches data from the given API URL and extracts the updated time and GBP rate.
    
    Parameters:
    api (str): The API URL to fetch data from.
    
    Returns:
    The updated time (str) and GBP rate (str), or (None, None) on error.
    """
    try:
        # Send a GET request to the API
        response_API = requests.get(api)
        # Raise an exception for HTTP errors
        response_API.raise_for_status()

        # Parse the JSON response
        data = response_API.json()
        
        # Extract the time the information was updated
        updated_time = data["time"]["updated"]
        
        # Extract the GBP rate
        gbp_rate = data["bpi"]["GBP"]["rate"]
        
        return updated_time, gbp_rate

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print("Error fetching data from API: {}".format(e))
        return None, None
    except KeyError:
        # Handle cases where the expected data structure is not present
        print("Error fetching data from API")
        return None, None

# Call the function with the API URL
updated_time, gbp_rate = extract_api_data(input_api_url)

if updated_time and gbp_rate:
    # Print the extracted information if successful
    print("Time Updated: {}".format(updated_time))
    print("GBP Rate: {}".format(gbp_rate))
else:
    # Inform the user if the data fetch was unsuccessful
    print("Failed to fetch data from API.")
