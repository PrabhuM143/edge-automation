from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set the correct path to the Edge WebDriver
edge_driver_path = 'C:/path/to/your/edgedriver/msedgedriver.exe'

# Initialize the Edge WebDriver with the specified options
edge_service = EdgeService(executable_path=edge_driver_path)
edge_options = EdgeOptions()

# Initialize the Edge WebDriver
driver = webdriver.Edge(service=edge_service, options=edge_options)

# Open Edge and navigate to Bing
driver.get("https://www.bing.com")

# Find the search box element
search_box = driver.find_element(By.NAME, "q")

# Perform the search
search_query = "OpenAI ChatGPT"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to see the results
time.sleep(5)

# Close the browser
driver.quit()
