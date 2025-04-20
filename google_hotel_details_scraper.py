from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

crawling_api = CrawlingAPI({ 'token': 'CRAWLBASE_JS_TOKEN' })

def make_crawlbase_request(url):
    response = crawling_api.get(url)
    if response['headers']['pc_status'] == '200':
        return response['body'].decode('utf-8')
    return None

def parse_hotel_details(hotel_url):
    html = make_crawlbase_request(hotel_url)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    name = soup.find("h1", class_="FNkAEc")
    price = soup.find("span", class_="qQOQpe prxS3d")
    rating = soup.find("span", class_="KFi5wf lA0BZ")
    reviews = soup.find("span", class_="jdzyld XLC8M")
    hotel_type = soup.find("span", class_="CFH2De")

    address = "N/A"
    contact = "N/A"

    location_section = soup.find_all("div", class_="K4nuhf")
    if location_section:
        spans = location_section[0].find_all("span")
        if len(spans) >= 3:
            address = spans[0].text
            contact = spans[2].text

    return {
        "name": name.text if name else "N/A",
        "price": price.text if price else "N/A",
        "rating": rating.text if rating else "N/A",
        "no_of_reviews": reviews.text if reviews else "N/A",
        "hotel_type": hotel_type.text if hotel_type else "N/A",
        "address": address,
        "contact": contact,
        "link": hotel_url
    }

def save_detailed_data(hotel_details, filename="google_hotel_details.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(hotel_details, f, ensure_ascii=False, indent=2)

def main():
    # Example input list from listings scraper
    hotel_links = [
        "https://www.google.com/travel/search?q=New%20York&qs=MihDaG9JeFBLSXpvWDR6SWZMQVJvTkwyY3ZNVEZ3ZDJnMU4yYzFOUkFCOAA&currency=USD&ved=2ahUKEwiY1rucg9CMAxUIAPkAHXyaE5EQyvcEegQIAxA-&ap=KigKEgm4tF8JXhxEQBF5jsg3iI5SwBISCfZ7hYTLm0RAEXmOyLfKcVLA&ts=CAESCgoCCAMKAggDEAAaXAo-EjwKCS9tLzAyXzI4NjIlMHg4OWMyNGZhNWQzM2YwODNiOjB4YzgwYjhmMDZlMTc3ZmU2MjoITmV3IFlvcmsSGhIUCgcI6Q8QBBgQEgcI6Q8QBBgRGAEyAhAAKgcKBToDVVNE",
        "https://www.google.com/travel/search?q=New%20York&qs=MidDaGtJZ0t6dDBjdkZ6dG1jQVJvTUwyY3ZNWEUxWW14eWF6a3pFQUU4AA&currency=USD&ved=2ahUKEwiY1rucg9CMAxUIAPkAHXyaE5EQyvcEegQIAxBV&ap=KigKEgm4tF8JXhxEQBF5jsg3iI5SwBISCfZ7hYTLm0RAEXmOyLfKcVLA&ts=CAESCgoCCAMKAggDEAAaXAo-EjwKCS9tLzAyXzI4NjIlMHg4OWMyNGZhNWQzM2YwODNiOjB4YzgwYjhmMDZlMTc3ZmU2MjoITmV3IFlvcmsSGhIUCgcI6Q8QBBgQEgcI6Q8QBBgRGAEyAhAAKgcKBToDVVNE"
    ]

    detailed_hotels = []

    for url in hotel_links:
        data = parse_hotel_details(url)
        if data:
            detailed_hotels.append(data)

    save_detailed_data(detailed_hotels)
    print(f"Saved details of {len(detailed_hotels)} hotels to google_hotel_details.json")

if __name__ == "__main__":
    main()