"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Write your solution here. Don't forget to return the result at the end."""
    my_ip= requests.get("https://api.ipify.org/?format=json", timeout=10) #get ip address
    jmy_ip=my_ip.json()     #convert response to json
    str_ip=str(jmy_ip['ip']) #strigify ip value
    info=requests.get(f"https://ipinfo.io/{str_ip}/geo", timeout=10)
    return info.json()


if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
