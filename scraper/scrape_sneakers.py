import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://sneakernews.com/release-dates/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []

# Update the selector based on the current HTML structure
for post in soup.select("div.release-card"):
    name_tag = post.select_one("h2.headline")
    link_tag = post.select_one("a")
    image_tag = post.select_one("img")
    date_tag = post.select_one("div.release-date")

    if name_tag and link_tag and image_tag and date_tag:
        try:
            release_date = datetime.strptime(date_tag.get_text(strip=True), "%B %d, %Y")
            results.append({
                "name": name_tag.get_text(strip=True),
                "url": link_tag['href'],
                "image": image_tag['src'],
                "release_date": release_date.isoformat()
            })
        except Exception as e:
            print(f"Skipping due to error: {e}")

# Sort by soonest release date
results.sort(key=lambda x: x['release_date'])

# Write the top 10 drops to a JSON file
with open("top10_drops.json", "w") as f:
    json.dump(results[:10], f, indent=2)
