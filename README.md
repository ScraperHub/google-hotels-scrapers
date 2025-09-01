<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>

# 🏨 Google Hotels Scraper with Python + Crawlbase

This repository contains two powerful web scrapers for extracting hotel data from Google Hotels using the Crawlbase Crawling API:

- 🔍 **Hotel Listings Scraper** – Collect hotel names, prices, ratings, and links from search results.

- 🏷️ **Hotel Detail Page Scraper** – Visit each hotel’s page to extract detailed info like address, contact, and more.

📖 Read the full tutorial → [How to Scrape Google Hotels with Python](https://crawlbase.com/)

## 🔧 Tools Used

- [`crawlbase`](https://pypi.org/project/crawlbase/) – to access Crawlbase Crawling API

- `BeautifulSoup` – for HTML parsing

- `json` – for structured data storage

- `Python 3.6+`

## 📦 Installation

Install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

## 🗺️ Scraper 1: Google Hotels Listings Scraper

**File:** `google_hotels_listings_scraper.py`

### ✅ What It Does

- Scrapes hotel listings from Google Hotels for a given location.
- Supports pagination by simulating clicks on the “Next” button.
- Saves the scraped data to `google_hotels.json`.

### ⚙️ How to Use

1. Replace `CRAWLBASE_JS_TOKEN` with your Crawlbase token.
2. Run the script:

```bash
python google_hotels_listings_scraper.py
```

### 🧪 Sample Output

```json
[
  {
    "name": "The Plaza Hotel",
    "price": "$784",
    "rating": "4.6",
    "link": "https://www.google.com/travel/hotels/..."
  },
  ...
]
```

## 🏷️ Scraper 2: Google Hotel Detail Page Scraper

**File:** `google_hotel_details_scraper.py`

### ✅ What It Does

- Takes individual hotel URLs and scrapes additional details such as:

  - Address
  - Contact Info
  - Number of Reviews
  - Hotel Type

- Saves the results to `google_hotel_details.json`.

### ⚙️ How to Use

1. Replace `CRAWLBASE_JS_TOKEN` with your Crawlbase token.
2. Add a list of hotel URLs (you can reuse results from the listings scraper).
3. Run the script:

```bash
python google_hotel_details_scraper.py
```

### 🧪 Sample Output

```json
[
  {
    "name": "The Plaza Hotel",
    "price": "$784",
    "rating": "4.6",
    "no_of_reviews": "1,234 reviews",
    "hotel_type": "5-star hotel",
    "address": "768 5th Ave, New York, NY 10019",
    "contact": "+1 212-759-3000",
    "link": "https://www.google.com/travel/hotels/..."
  },
  ...
]
```

## 🧠 Pro Tips

- Increase max_pages in the listings scraper to collect more data.
- Use output from listings as input to the detail scraper.
- Combine both scripts into a pipeline for full automation.
