"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    response = requests.get("http://ip-api.com/json/")
    data = response.json()
    ip_address = data.get("query")
    city = data.get("city")
    region = data.get("region")
    country = data.get("country")
    loc = data.get("lon")
    org = data.get("org")
    return {
    "ip": ip_address,
    "city": city,
    "region": region,
    "country": country,
    "loc": loc,
    "org": org
}
if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
