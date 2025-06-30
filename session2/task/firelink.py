"""List of the favourite websites."""
import webbrowser
favourite_websites_list = [
    "https://www.facebook.com/",
    "https://github.com/",
    "https://www.linkedin.com/"
]

def firefox(website_url):
    """Open the website."""
    webbrowser.open(website_url)
