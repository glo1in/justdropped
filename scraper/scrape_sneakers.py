import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://sneakernews.com/release-dates/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

results = []
for post in soup.select(".release-list .post"):
    name = post.select_one(".headline a")
    image = post.select_one("img")
    date = post.select_one(".release-date")
    if name and image and date:
        results.append({
            "name": name.get_text(strip=True),
            "url": name['href'],
            "image": image['src'],
            "release_date": datetime.strptime(date.get_text(strip=True), "%B %d, %Y").isoformat()
        })

# Sort by soonest
results.sort(key=lambda x: x['release_date'])

# ✅ Output file now saved to project root
with open("top10_drops.json", "w") as f:
    json.dump(results[:10], f, indent=2)
