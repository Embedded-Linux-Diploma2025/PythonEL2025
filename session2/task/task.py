"""List of the favourite websites."""
import firelink

def print_favourite_websites(fav_websites_list):
    """Print the websites."""
    for websire_number, website_url in enumerate(fav_websites_list):
        print(f"website number {websire_number + 1} is {website_url}")

print_favourite_websites(firelink.favourite_websites_list)
website_num = input("enter the website number to open: ")

firelink.firefox(firelink.favourite_websites_list[int(website_num) - 1])
