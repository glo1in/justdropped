import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_sneakerfreaker():
    URL = "https://www.sneakerfreaker.com/releases/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    drops = []
    for card in soup.select("div.card"):
        try:
            name_tag = card.select_one("h2.card__title")
            link_tag = card.select_one("a.card__link")
            image_tag = card.select_one("img.card__image")
            date_tag = card.select_one("div.card__date")
            if name_tag and link_tag and image_tag and date_tag:
                raw_date = date_tag.get_text(strip=True)
                parsed_date = datetime.strptime(raw_date, "%d %b %y")
                drops.append({
                    "name": name_tag.get_text(strip=True),
                    "url": "https://www.sneakerfreaker.com" + link_tag["href"],
                    "image": image_tag["src"],
                    "release_date": parsed_date.isoformat()
                })
        except Exception as e:
            print("Error:", e)

    drops.sort(key=lambda x: x["release_date"])
    with open("public/top10_drops.json", "w") as f:
        json.dump(drops[:10], f, indent=2)

    print(f"✅ Scraped and saved {len(drops[:10])} drops")

if __name__ == "__main__":
    scrape_sneakerfreaker()