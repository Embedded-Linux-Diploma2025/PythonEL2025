"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Gets location information based on public IP address.

    Uses the ipinfo.io API to fetch location data.

    Returns:
        dict: A dictionary containing location information such as
              ip, city, region, country, etc. Returns an empty
              dictionary if the request fails.
    """
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        # print(response.json())
        return response.json()
    except requests.exceptions.RequestException as exception:
        print(f"Error fetching location data: {exception}")
        return {}


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
