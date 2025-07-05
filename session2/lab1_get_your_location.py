"""Write a Python program to get info about your location."""

import requests

def get_info_location()->dict:
    """Write your solution here. Don't forget to return the result at the end."""
    url=requests.get("https://api.ipify.org/?gormat=json",timeout=20)
    loc=requests.get(f"https://ipinfo.io/{url.text}/geo" ,timeout=20)
    # print(type(loc.json()))
    # print(loc.json())
    return loc.json()

# url=requests.get("https://api.ipify.org/?gormat=json")
# print(url.text)

# loc=requests.get(f"https://ipinfo.io/{url.text}/geo")
# print(location_info.text)
# print(location_info.json())

location_info =get_info_location()
print(location_info)

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
    # print("ALL Tests Has Passed")
