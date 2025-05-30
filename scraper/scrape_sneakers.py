import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://www.nicekicks.com/release-dates/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

drops = []

for card in soup.select("div.card-release"):
    try:
        name_tag = card.select_one(".release-title")
        link_tag = card.select_one("a")
        image_tag = card.select_one("img")
        date_tag = card.select_one(".date")

        if name_tag and link_tag and image_tag and date_tag:
            raw_date = date_tag.get_text(strip=True)
            try:
                parsed_date = datetime.strptime(raw_date, "%B %d, %Y")
            except ValueError:
                continue

            drops.append({
                "name": name_tag.get_text(strip=True),
                "url": link_tag["href"],
                "image": image_tag["data-src"] if image_tag.has_attr("data-src") else image_tag["src"],
                "release_date": parsed_date.isoformat()
            })
    except Exception as e:
        print("❌ Skipping a card due to error:", e)

# Sort and save
drops.sort(key=lambda x: x["release_date"])
with open("top10_drops.json", "w") as f:
    json.dump(drops[:10], f, indent=2)

print(f"✅ Scraped and saved {len(drops[:10])} drops from Nice Kicks")
