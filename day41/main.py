#Hyper Text-  The pieces of text which can linke to ohter documents in the website

import os
import time
import logging
from datetime import datetime
import schedule
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import pandas as pd

# Configure logging
logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the output directory
OUTPUT_DIR = r"C:\Documents\exel file from bot"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def init_driver():
    print("Initializing WebDriver...")
    options = FirefoxOptions()
    options.add_argument('-headless')
    return webdriver.Firefox(options=options)

def get_areas(driver, city):
    print(f"Searching for areas in {city}")
    driver.get("https://www.google.com/maps")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "searchboxinput"))
    )
    search_box.clear()
    search_box.send_keys(f"areas in {city}")
    search_box.send_keys(Keys.ENTER)
    time.sleep(15)  # Wait for results to load

    areas = []
    try:
        area_elements = driver.find_elements(By.CSS_SELECTOR, "div.Nv2PK")
        for element in area_elements[:5]:  # Limit to first 5 areas
            try:
                area_name = element.find_element(By.CSS_SELECTOR, "div.qBF1Pd").text
                areas.append(area_name)
                print(f"Found area: {area_name}")
            except NoSuchElementException:
                continue
    except Exception as e:
        print(f"Error finding areas: {str(e)}")
    
    return areas

def search_and_scrape(driver, entity, city, area):
    try:
        print(f"Searching for {entity} in {area}, {city}")
        driver.get("https://www.google.com/maps")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        search_box.clear()
        search_box.send_keys(f"{entity} in {area}, {city}")
        search_box.send_keys(Keys.ENTER)
        time.sleep(15)  # Wait for results to load

        # Scroll to load more results
        scrollable_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label^='Results for']"))
        )
        last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        
        for _ in range(5):  # Scroll 5 times
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scrollable_div)
            time.sleep(20)  # Wait for new results to load
            new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
            if new_height == last_height:
                break
            last_height = new_height

        results = []
        elements = driver.find_elements(By.CSS_SELECTOR, "div.Nv2PK")
        print(f"Found {len(elements)} elements")
        for element in elements:
            try:
                name = element.find_element(By.CSS_SELECTOR, "div.qBF1Pd").text
                rating_element = element.find_elements(By.CSS_SELECTOR, "span.MW4etd")
                rating = rating_element[0].text if rating_element else "N/A"
                link = element.find_element(By.CSS_SELECTOR, "a.hfpxzc").get_attribute("href")
                results.append({"name": name, "rating": rating, "link": link, "area": area})
                print(f"Extracted: {name}")
            except (NoSuchElementException, StaleElementReferenceException) as e:
                print(f"Error extracting element: {str(e)}")
                continue

        return results
    except Exception as e:
        print(f"Error during scraping: {str(e)}")
        logging.error(f"Error during scraping: {str(e)}")
        return []

def save_to_excel(data, filename):
    full_path = os.path.join(OUTPUT_DIR, filename)
    print(f"Saving data to {full_path}")
    df = pd.DataFrame(data)
    df.to_excel(full_path, index=False, engine='openpyxl')
    print(f"Data saved successfully to {full_path}")

def run_scraper(city, entity):
    print(f"Running scraper for {entity} in {city}")
    driver = init_driver()
    all_results = []

    try:
        areas = get_areas(driver, city)
        if not areas:
            print(f"No areas found for {city}. Searching in the city center.")
            areas = [city]

        for area in areas:
            print(f"Scraping {entity} in {area}, {city}")
            results = search_and_scrape(driver, entity, city, area)
            all_results.extend(results)
            print(f"Found {len(results)} results in {area}")

        if all_results:
            filename = f"{city}_{entity}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            save_to_excel(all_results, filename)
            print(f"Scraping completed successfully. Results saved to {filename}")
            logging.info(f"Scraping completed. Results saved to {filename}")
        else:
            print("No results found.")
            logging.warning("No results found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        logging.error(f"An error occurred: {str(e)}")

    finally:
        driver.quit()

def parse_time(time_str):
    try:
        # Try parsing as 24-hour format
        return datetime.strptime(time_str, "%H:%M").strftime("%H:%M")
    except ValueError:
        try:
            # Try parsing as 12-hour format
            return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")
        except ValueError:
            raise ValueError("Invalid time format. Please use either HH:MM (24-hour) or HH:MM AM/PM (12-hour) format.")

def main():
    print("Setting up the scraper scheduler...")
    city = input("Enter the city name: ")
    entity = input("Enter the entity to search for (e.g., hotels, restaurants): ")
    schedule_time = input("Enter the time to run the scraper daily (HH:MM in 24-hour format or HH:MM AM/PM): ")

    try:
        schedule_time_24h = parse_time(schedule_time)
        schedule.every().day.at(schedule_time_24h).do(run_scraper, city, entity)

        print(f"Scraper scheduled to run daily at {schedule_time_24h} for {entity} in {city}")
        print("Keep the script running to execute the scheduled task.")
        print("Press Ctrl+C to stop the script.")

        while True:
            schedule.run_pending()
            time.sleep(10)
    except ValueError as e:
        print(f"Error: {str(e)}")
        print("Please run the script again with a valid time format.")

if __name__ == "__main__":
    main()