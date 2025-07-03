"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    # Get public IP address
    url = requests.get("http://api.ipify.org/?format=json",timeout=5)
    url.raise_for_status()
    # ip_data is a dict
    ip_data = url.json()
    ip = ip_data["ip"]

    # Get location information using the IP address
    location_response = requests.get(f"https://ipinfo.io/{ip}/json",timeout=5)
    location_response.raise_for_status()
    location_data = location_response.json()
    # print dict content
    for i in location_data :
        print(f"{i} : {location_data.get(i)}")
    return location_data


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
