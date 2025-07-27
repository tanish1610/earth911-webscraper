import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up the driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Optional: run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Go to the target URL
driver.get("https://search.earth911.com/?what=Electronics&where=10001&list_filter=all&max_distance=100")

# Wait for content to load
time.sleep(5)  # Adjust as needed for your internet speed

# Find result containers
facilities = driver.find_elements(By.CSS_SELECTOR, "div.list-result-item")[:3]

data = []

for facility in facilities:
    try:
        business_name = facility.find_element(By.CSS_SELECTOR, "h2").text.strip()
        address = facility.find_element(By.CSS_SELECTOR, "p.result-address").text.strip()
        materials = facility.find_element(By.CSS_SELECTOR, "div.result-materials").text.strip().replace('\n', ', ')
        last_update = facility.find_element(By.CSS_SELECTOR, "div.result-date").text.strip().replace("Last updated: ", "")
        
        data.append([business_name, last_update, address, materials])
    except Exception as e:
        print("Error while extracting:", e)

driver.quit()

# Write to CSV
with open("earth911_recycling_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["business_name", "last_update_date", "street_address", "materials_accepted"])
    writer.writerows(data)

print("CSV file generated: earth911_recycling_data.csv")
