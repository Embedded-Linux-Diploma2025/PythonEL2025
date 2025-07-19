"""Write a Python program to get info about your location."""

import requests

def get_info_location():
    """Get location info using an IP-based API and return it as a dictionary."""
    response = requests.get("https://ipinfo.io/json")
    return response.json()

if __name__ == "__main__":
    location_info = get_info_location()

    
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"

    print("All test cases passed ✅")
