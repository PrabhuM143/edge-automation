from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace 'path_to_your_webdriver' with the actual path to your Edge WebDriver
webdriver_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"

# Initialize Edge WebDriver
try:
    service = Service(webdriver_path)
    driver = webdriver.Edge(service=service)
except Exception as e:
    print(f"Failed to start WebDriver: {e}")
    exit(1)

# List of custom 50 searches
search_queries = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Andaman and Nicobar Islands",
    "Chandigarh"
]


# Open Edge browser and perform searches
try:
    for query in search_queries:
        # Open Bing search
        driver.get("https://www.bing.com")
        time.sleep(2)  # Wait for the page to load

        # Find the search box and enter the search query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for search results to load

        # Open the first search result link
        first_result = driver.find_element(By.CSS_SELECTOR, "li.b_algo h2 a")
        first_result.click()
        time.sleep(3)  # Keep the page open for 3 seconds

        # Check if a new tab was opened
        if len(driver.window_handles) > 1:
            driver.close()  # Close the new tab
            driver.switch_to.window(driver.window_handles[0])  # Switch back to the original tab

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
