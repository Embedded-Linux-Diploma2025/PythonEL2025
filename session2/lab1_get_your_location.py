"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    # url = requests.get("https://api.ipify.org/?format=json")
    # print(url.json())  # ip = 197.58.108.252
    try:
        response = requests.get('https://ipinfo.io/197.58.108.252/geo' , timeout=5)
        # response = requests.get('https://ipinfo.io/json', timeout=5)
        response.raise_for_status()
        data = response.json()
        # print(f"data is{data}")
        return {
            'ip': data.get('ip', ''),
            'city': data.get('city', ''),
            'region': data.get('region', ''),
            'country': data.get('country', ''),
            'loc': data.get('loc', ''),
            'org': data.get('org', '')
        }
    except requests.RequestException:
        # print(" enter the exception")
        return {
            'ip': '',
            'city': '',
            'region': '',
            'country': '',
            'loc': '',
            'org': ''
        }


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
