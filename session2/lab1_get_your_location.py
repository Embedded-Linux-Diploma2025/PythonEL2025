"""Write a Python program to get info about your location."""

from urllib.request import urlopen
import re as r
import requests



def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""

    with urlopen('http://checkip.dyndns.com/') as getip:
        info = str(getip.read())

    ip = r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(info).group(1)
    url = requests.get(f"https://ipinfo.io/{ip}/geo", timeout=10)

    return url.json()  

if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
