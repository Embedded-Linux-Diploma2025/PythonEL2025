"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """ Fetches information about the current IP address location """
    url = requests.get("https://api.ipify.org/?format=json", timeout=5)
    api = url.json()
    return requests.get(f"https://ipinfo.io/{api['ip']}/geo", timeout=5).json()


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
