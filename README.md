# Earth911 Web Scraper – Python Task

This project is a short technical task to scrape recycling facility data from [Earth911 Recycling Center Search](https://search.earth911.com/) using Selenium.

## 📌 Task Details

Search Term: **Electronics**  
Zip Code: **10001**  
Radius: **Within 100 miles**

### Extracted Fields:
- business_name
- last_update_date
- street_address
- materials_accepted

## ✅ Output

Output saved as: `earth911_recycling_data.csv`  
Includes 3 sample facility entries.

## 🛠️ Tools & Libraries Used

- **Selenium** – For interacting with the dynamic webpage
- **WebDriver Manager** – For handling ChromeDriver
- **CSV module** – To store structured data

## 🧠 Scraping Logic

- Launched the Earth911 URL with query parameters.
- Waited for JS content to load (`time.sleep`).
- Extracted 3 facility blocks using class selectors.
- Parsed and cleaned the required fields.
- Saved structured data in CSV format.

## ⚠️ Challenges and Handling

- Dynamic content loading: handled via Selenium instead of BeautifulSoup.
- Error handling: try-except blocks in place for partial data or layout issues.
