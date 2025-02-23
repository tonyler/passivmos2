import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file_path = 'selectors.json'
with open(file_path, 'r') as file:
    config = json.load(file)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Disable GPU
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-notifications")  # Disable notifications

def scrape_prices():
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("WebDriver initialized successfully for prices.")
    except WebDriverException as e:
        print(f"Error initializing WebDriver: {e}")
        exit(1)
        
    driver.get('https://restake.app/')
    driver.maximize_window()
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[1]/div[2]/div/div[3]/a'))
    )
    element.click()
    
    prices_dict = {}
    for project in config['projects']: 
        try:
            price = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, config['projects'][project]["selector_price"]))
            )
            prices_dict[project] = float(price.text.replace("$", ""))
        except Exception as e:  
            print(f"Error scraping price for {project}: {e}")
            prices_dict[project] = 0.0
            continue
    driver.quit()
    
    return prices_dict
