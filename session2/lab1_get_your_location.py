"""Write a Python program to get info about your location."""
import requests
def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    url ="https://ipinfo.io/json"
    my_info =requests.get(url, timeout= 4)
    return my_info.json()

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
