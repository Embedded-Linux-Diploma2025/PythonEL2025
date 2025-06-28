"""Write a Python program to get info about your location."""

import requests

def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    response_content = requests.get('http://ip-api.com/json/24.48.0.1',timeout=5).json()
    response_dic = {
        "ip":response_content["query"],
        "city":response_content["city"],
        "region":response_content["region"],
        "country":response_content["country"],
        "loc":"1",
        "org":response_content["org"]
    }
    return response_dic
if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
