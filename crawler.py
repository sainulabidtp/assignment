import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Create a directory for storing the downloaded images
if not os.path.exists("images"):
    os.makedirs("images")

# URL of the website to scrape
url = "https://www.gettyimages.in/photos/aamir-khan-actor"

# Send a GET request to the website
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img")

    # Counter for naming the downloaded images
    count = 1

    for image in images:
        # Get the source URL of the image
        image_url = image["src"]

        # Download only the smaller images
        if "media.gettyimages" in image_url and "s=612x612" in image_url:
            # Extract the filename from the URL
            parsed_url = urlparse(image_url)
            filename = os.path.basename(parsed_url.path)
            filename = filename.split("?")[0]

            # Generate the pathname for the image
            pathname = filename.split(".")[0]

            # Download the image and save it with the generated filename
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(f"images/{pathname}.jpg", "wb") as f:
                    f.write(response.content)
                    print(f"Downloaded image {count}")
                    count += 1
            else:
                print(f"Failed to download image {count}")
else:
    print("Failed to retrieve website content")
