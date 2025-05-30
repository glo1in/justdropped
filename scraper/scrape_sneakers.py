import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time
import re
import os

class SneakerScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.releases = []
    
    def scrape_nike_snkrs(self):
        """Scrape Nike SNKRS for upcoming releases"""
        print("🔍 Scraping Nike SNKRS...")
        try:
            # Simulating Nike SNKRS data (actual scraping would require handling their API/dynamic content)
            nike_releases = [
                {
                    "brand": "Nike",
                    "name": "Air Jordan 1 Retro High OG 'Chicago Lost and Found'",
                    "price": "$170",
                    "release_date": "2024-01-15",
                    "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/61734ec7-dad8-40f3-9b95-c7500939150a/air-jordan-1-retro-high-og-shoes-Pph9wD.png",
                    "website": "Nike SNKRS",
                    "hype_level": 9
                },
                {
                    "brand": "Nike",
                    "name": "Nike Dunk Low 'Panda'",
                    "price": "$100",
                    "release_date": "2024-01-20",
                    "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/dd1391-100/dunk-low-shoes-5FQWGR.png",
                    "website": "Nike SNKRS",
                    "hype_level": 7
                },
                {
                    "brand": "Nike",
                    "name": "Air Jordan 3 Retro 'White Cement'",
                    "price": "$200",
                    "release_date": "2024-01-12",
                    "image_url": "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/136064-104/air-jordan-3-retro-shoes-NIke02.png",
                    "website": "Nike SNKRS",
                    "hype_level": 10
                }
            ]
            self.releases.extend(nike_releases)
            print(f"✅ Found {len(nike_releases)} Nike releases")
        except Exception as e:
            print(f"❌ Error scraping Nike: {e}")
    
    def scrape_adidas(self):
        """Scrape Adidas for upcoming releases"""
        print("🔍 Scraping Adidas...")
        try:
            # Simulating Adidas data
            adidas_releases = [
                {
                    "brand": "Adidas",
                    "name": "Yeezy Boost 350 V2 'Bone'",
                    "price": "$230",
                    "release_date": "2024-01-18",
                    "image_url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/8a2f41f6f9d04d6a8c5aaf8d00e8c7e2_9366/Yeezy_Boost_350_V2_Shoes_White_HQ4540_01_standard.jpg",
                    "website": "Adidas",
                    "hype_level": 8
                },
                {
                    "brand": "Adidas",
                    "name": "Forum Low 'Cloud White'",
                    "price": "$90",
                    "release_date": "2024-01-22",
                    "image_url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/28b0f1c6c8a64d6f9c5aaf8d00e8c7e2_9366/Forum_Low_Shoes_White_FY7757_01_standard.jpg",
                    "website": "Adidas",
                    "hype_level": 5
                },
                {
                    "brand": "Adidas",
                    "name": "Yeezy Slide 'Granite'",
                    "price": "$90",
                    "release_date": "2024-01-16",
                    "image_url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/granite-yeezy-slide/Yeezy_Slide_Granite_ID2349_01_standard.jpg",
                    "website": "Adidas",
                    "hype_level": 6
                }
            ]
            self.releases.extend(adidas_releases)
            print(f"✅ Found {len(adidas_releases)} Adidas releases")
        except Exception as e:
            print(f"❌ Error scraping Adidas: {e}")
    
    def scrape_footlocker(self):
        """Scrape Foot Locker for upcoming releases"""
        print("🔍 Scraping Foot Locker...")
        try:
            # Simulating Foot Locker data
            footlocker_releases = [
                {
                    "brand": "Jordan",
                    "name": "Air Jordan 4 Retro 'Black Cat'",
                    "price": "$210",
                    "release_date": "2024-01-25",
                    "image_url": "https://images.footlocker.com/is/image/FLEU/314254001_01?wid=581&hei=581&fmt=png-alpha",
                    "website": "Foot Locker",
                    "hype_level": 9
                },
                {
                    "brand": "Nike",
                    "name": "Air Max 90 'Infrared'",
                    "price": "$130",
                    "release_date": "2024-01-28",
                    "image_url": "https://images.footlocker.com/is/image/FLEU/325213126_01?wid=581&hei=581&fmt=png-alpha",
                    "website": "Foot Locker",
                    "hype_level": 7
                }
            ]
            self.releases.extend(footlocker_releases)
            print(f"✅ Found {len(footlocker_releases)} Foot Locker releases")
        except Exception as e:
            print(f"❌ Error scraping Foot Locker: {e}")
    
    def scrape_stockx(self):
        """Scrape StockX for trending releases"""
        print("🔍 Scraping StockX...")
        try:
            # Simulating StockX data
            stockx_releases = [
                {
                    "brand": "Travis Scott",
                    "name": "Travis Scott x Air Jordan 1 Low OG 'Olive'",
                    "price": "$1,500",
                    "release_date": "2024-02-01",
                    "image_url": "https://images.stockx.com/images/Air-Jordan-1-Low-OG-SP-Travis-Scott-Olive.jpg",
                    "website": "StockX",
                    "hype_level": 10
                },
                {
                    "brand": "Off-White",
                    "name": "Off-White x Nike Dunk Low 'Pine Green'",
                    "price": "$2,200",
                    "release_date": "2024-02-05",
                    "image_url": "https://images.stockx.com/images/Nike-Dunk-Low-Off-White-Pine-Green.jpg",
                    "website": "StockX",
                    "hype_level": 10
                }
            ]
            self.releases.extend(stockx_releases)
            print(f"✅ Found {len(stockx_releases)} StockX releases")
        except Exception as e:
            print(f"❌ Error scraping StockX: {e}")
    
    def scrape_goat(self):
        """Scrape GOAT for upcoming releases"""
        print("🔍 Scraping GOAT...")
        try:
            # Simulating GOAT data
            goat_releases = [
                {
                    "brand": "New Balance",
                    "name": "New Balance 550 'White Green'",
                    "price": "$110",
                    "release_date": "2024-02-08",
                    "image_url": "https://image.goat.com/attachments/product_template_pictures/images/008/654/900/original/550_White_Green.png",
                    "website": "GOAT",
                    "hype_level": 6
                },
                {
                    "brand": "Converse",
                    "name": "Converse Chuck 70 High 'Comme des Garçons'",
                    "price": "$150",
                    "release_date": "2024-02-10",
                    "image_url": "https://image.goat.com/attachments/product_template_pictures/images/008/654/901/original/Chuck_70_CDG.png",
                    "website": "GOAT",
                    "hype_level": 8
                },
                {
                    "brand": "Nike",
                    "name": "Nike Air Force 1 '07 'Triple White'",
                    "price": "$90",
                    "release_date": "2024-01-30",
                    "image_url": "https://image.goat.com/attachments/product_template_pictures/images/000/000/123/original/AF1_White.png",
                    "website": "GOAT",
                    "hype_level": 4
                }
            ]
            self.releases.extend(goat_releases)
            print(f"✅ Found {len(goat_releases)} GOAT releases")
        except Exception as e:
            print(f"❌ Error scraping GOAT: {e}")
    
    def format_release_date(self, date_str):
        """Format release date for better readability"""
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            return date_obj.strftime("%B %d, %Y")
        except:
            return date_str
    
    def get_top_10_drops(self):
        """Get top 10 releases based on hype level and release date"""
        if not self.releases:
            return []
        
        # Sort by hype level (descending) then by release date (ascending)
        sorted_releases = sorted(
            self.releases, 
            key=lambda x: (-x.get('hype_level', 0), x['release_date'])
        )
        
        # Return top 10
        return sorted_releases[:10]
    
    def save_top_10_to_json(self):
        """Save top 10 releases to top10_drops.json in root directory"""
        try:
            # Get top 10 releases
            top_10_releases = self.get_top_10_drops()
            
            # Create the output structure
            output_data = {
                "last_updated": datetime.now().isoformat(),
                "total_releases_found": len(self.releases),
                "top_10_drops": top_10_releases,
                "metadata": {
                    "scraper_version": "1.0",
                    "websites_scraped": ["Nike SNKRS", "Adidas", "Foot Locker", "StockX", "GOAT"],
                    "ranking_criteria": "Hype level and release date"
                }
            }
            
            # Get the root directory path
            root_dir = os.getcwd()
            file_path = os.path.join(root_dir, "top10_drops.json")
            
            # Save to JSON file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Top 10 drops saved to: {file_path}")
            print(f"📁 File location: {os.path.abspath(file_path)}")
            
            return file_path
            
        except Exception as e:
            print(f"❌ Error saving to JSON: {e}")
            return None
    
    def display_top_10_releases(self):
        """Display top 10 releases in a formatted way"""
        top_10 = self.get_top_10_drops()
        
        print("\n" + "="*80)
        print("🔥 TOP 10 UPCOMING SNEAKER DROPS 🔥")
        print("="*80)
        
        if not top_10:
            print("No releases found.")
            return
        
        for i, release in enumerate(top_10, 1):
            hype_stars = "⭐" * release.get('hype_level', 0)
            print(f"\n{i}. {release['name']}")
            print(f"   Brand: {release['brand']}")
            print(f"   Price: {release['price']}")
            print(f"   Release Date: {self.format_release_date(release['release_date'])}")
            print(f"   Website: {release['website']}")
            print(f"   Hype Level: {hype_stars} ({release.get('hype_level', 0)}/10)")
            print("-" * 60)
    
    def get_release_stats(self):
        """Display statistics about the scraped releases"""
        if not self.releases:
            return
        
        print(f"\n📊 RELEASE STATISTICS")
        print(f"Total releases found: {len(self.releases)}")
        print(f"Top 10 drops selected for JSON export")
        
        # Count by brand
        brands = {}
        websites = {}
        
        for release in self.releases:
            brand = release['brand']
            website = release['website']
            
            brands[brand] = brands.get(brand, 0) + 1
            websites[website] = websites.get(website, 0) + 1
        
        print(f"\nReleases by brand:")
        for brand, count in sorted(brands.items()):
            print(f"  {brand}: {count}")
        
        print(f"\nReleases by website:")
        for website, count in sorted(websites.items()):
            print(f"  {website}: {count}")
    
    def run_scraper(self):
        """Run the complete scraping process"""
        print("🚀 Starting sneaker release scraper...")
        print("Note: This is a demonstration with simulated data.")
        print("Real scraping would require handling dynamic content, APIs, and anti-bot measures.\n")
        
        # Scrape all websites
        self.scrape_nike_snkrs()
        time.sleep(1)  # Be respectful with requests
        
        self.scrape_adidas()
        time.sleep(1)
        
        self.scrape_footlocker()
        time.sleep(1)
        
        self.scrape_stockx()
        time.sleep(1)
        
        self.scrape_goat()
        
        # Display results
        self.display_top_10_releases()
        self.get_release_stats()
        
        # Save top 10 to JSON file in root directory
        json_file_path = self.save_top_10_to_json()
        
        if json_file_path:
            print(f"\n✅ Successfully created top10_drops.json with the hottest upcoming releases!")
            print(f"📄 File contains top 10 drops ranked by hype level and release date")

# Run the scraper
if __name__ == "__main__":
    scraper = SneakerScraper()
    scraper.run_scraper()
