from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import json

crawling_api = CrawlingAPI({ 'token': 'CRAWLBASE_JS_TOKEN' })

def make_crawlbase_request(url, css_click_element=None):
    try:
        options = {}

        if css_click_element:
            options['css_click_selector'] = css_click_element
            options['ajax_wait'] = 'true'

        response = crawling_api.get(url, options)
        if response['headers'].get('pc_status') == '200':
            return response['body'].decode('utf-8')

        return response

    except Exception as e:
        print(f"Error during Crawlbase request: {e}")
        return {}

def parse_hotel_listings(html):
    soup = BeautifulSoup(html, "html.parser")
    hotel_data = []

    hotels = soup.find_all("div", class_="BcKagd")
    for hotel in hotels:
        name = hotel.find("h2", class_="BgYkof")
        price = hotel.find("span", class_="qQOQpe prxS3d")
        rating = hotel.find("span", class_="KFi5wf lA0BZ")
        link = hotel.find("a", class_="PVOOXe")

        hotel_data.append({
            "name": name.text if name else "N/A",
            "price": price.text if price else "N/A",
            "rating": rating.text if rating else "N/A",
            "link": "https://www.google.com" + link["href"] if link else "N/A"
        })

    return hotel_data

def save_to_json(data, filename="google_hotels.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    url = "https://www.google.com/travel/hotels/New-York?q=New+York&currency=USD"
    all_hotels = []
    max_pages = 2
    page_count = 0

    while page_count < max_pages:
        html = ''

        if page_count == 0:
            # For 1st page
            html = make_crawlbase_request(url)
        else:
            # For next pages
            html = make_crawlbase_request(url, 'button[jsname="OCpkoe"]')

        if not html:
            break

        hotels = parse_hotel_listings(html)
        all_hotels.extend(hotels)

        page_count += 1

    save_to_json(all_hotels)
    print(f"Scraped {len(all_hotels)} hotels and saved to google_hotels.json")

if __name__ == "__main__":
    main()