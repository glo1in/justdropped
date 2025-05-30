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
        name = post.select_one("h2.headline a")
        image = post.select_one("img")
        date = post.select_one(".release-date")

        if name and image and date:
            try:
                parsed_date = datetime.strptime(date.get_text(strip=True), "%B %d, %Y")
                drops.append({
                    "name": name.get_text(strip=True),
                    "url": name["href"],
                    "image": image["src"],
                    "release_date": parsed_date.isoformat()
                })
            except Exception:
                continue
    return drops

# Run and save top 10 drops
if __name__ == "__main__":
    results = scrape_sneakernews()
    results.sort(key=lambda x: x['release_date'])

    with open("top10_drops.json", "w") as f:
        json.dump(results[:10], f, indent=2)

    print("Saved top10_drops.json with", len(results[:10]), "entries")
