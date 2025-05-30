import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_sneakernews():
    URL = "https://sneakernews.com/release-dates/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    drops = []

    for post in soup.select("article"):
        name_tag = post.select_one("h2.headline a")
        image_tag = post.select_one("img")
        date_tag = post.select_one(".release-date")

        if name_tag and image_tag and date_tag:
            try:
                release_date = datetime.strptime(date_tag.get_text(strip=True), "%B %d, %Y")
                drops.append({
                    "name": name_tag.get_text(strip=True),
                    "url": name_tag["href"],
                    "image": image_tag["src"],
                    "release_date": release_date.isoformat()
                })
            except Exception as e:
                print("Error parsing date:", e)

    print(f"✅ Scraped {len(drops)} sneaker drops")
    for drop in drops[:3]:  # preview first 3 entries
        print(json.dumps(drop, indent=2))

    return drops

if __name__ == "__main__":
    results = scrape_sneakernews()
    results.sort(key=lambda x: x['release_date'])

    with open("top10_drops.json", "w") as f:
        json.dump(results[:10], f, indent=2)

    print("✅ Saved top10_drops.json with", len(results[:10]), "items")
