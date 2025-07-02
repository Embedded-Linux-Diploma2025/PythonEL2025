"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    response = requests.get("https://ipinfo.io/json",timeout=10)
    data = response.json()
    # print(f"IP: {data.get('ip')}")
    # print(f"City: {data.get('city')}")
    # print(f"Region: {data.get('region')}")
    # print(f"Country: {data.get('country')}")
    # print(f"Location: {data.get('loc')}")
    # print(f"Org: {data.get('org')}")
    return data


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
