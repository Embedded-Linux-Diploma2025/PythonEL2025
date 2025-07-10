"""Write a Python program to get info about your location."""

import requests


def get_info_location():
    """Get location info from ipinfo.io with error handling."""
    url = 'https://ipinfo.io/json'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise HTTPError if response is 4xx or 5xx
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("❌ Request timed out.")
    except requests.exceptions.ConnectionError:
        print("❌ Network connection error.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Other request exception: {e}")
    except ValueError:
        print("❌ Failed to parse JSON.")

    return None  # In case of any error



if __name__ == "__main__":
    location_info = get_info_location()
    assert "ip" in location_info, "Test case failed"
    assert "city" in location_info, "Test case failed"
    assert "region" in location_info, "Test case failed"
    assert "country" in location_info, "Test case failed"
    assert "loc" in location_info, "Test case failed"
    assert "org" in location_info, "Test case failed"
