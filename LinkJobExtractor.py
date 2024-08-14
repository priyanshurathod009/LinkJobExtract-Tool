import logging
import time
import os
import pandas as pd
from selenium.common.exceptions import JavascriptException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData, EventMetrics
from linkedin_jobs_scraper.query import Query, QueryOptions
from retrying import retry
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize an empty list to store job data
job_data = []

def on_data(data: EventData):
    """Process job data."""
    try:
        job_info = {
            'Title': data.title,
            'Company': data.company,
            #'Company Link': data.company_link,
            'Date': data.date,
            'Link': data.link,
            'Description Length': len(data.description),
            'Skills': data.skills,
            #'Apply-link': data.apply_link,
            'Place': data.place,
            'Location': data.location,
            'Query': data.query
        }
        job_data.append(job_info)
        logging.info(f"Processed job data: {job_info}")
    except Exception as e:
        logging.error(f"Error processing data: {e}")

def on_metrics(metrics: EventMetrics):
    """Handle metrics data."""
    try:
        logging.info(f'[ON_METRICS] {metrics}')
        time.sleep(200)  # Sleep for 200 seconds between pages
    except Exception as e:
        logging.error(f"Error handling metrics: {e}")

def on_error(error):
    """Handle errors."""
    try:
        logging.error(f'[ON_ERROR] {error}')
        if isinstance(error, JavascriptException):
            logging.warning('JavaScript error encountered. Check element selectors or page state.')
        elif isinstance(error, TimeoutException):
            logging.warning('Timeout error encountered. Retrying...')
        time.sleep(125)  # Sleep for 125 seconds if an error occurs
    except Exception as e:
        logging.error(f"Error handling error: {e}")

def on_end():
    """Save collected data to a CSV file."""
    try:
        # Define the directory and file path
        directory = 'C:/Users/priya/VS_Files/New folder (2)'
        file_path = os.path.join(directory, f'job_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
        
        # Create directory if it does not exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Save data to CSV
        df = pd.DataFrame(job_data)
        df.to_csv(file_path, index=False)
        logging.info(f'Data saved to {file_path}')
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")

def wait_for_element(driver, selector, timeout=20):
    """Wait for an element to be present on the page."""
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
    except TimeoutException as e:
        logging.error(f"Timeout while waiting for element: {selector}. Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error while waiting for element: {selector}. Error: {e}")
        raise

# Configure the scraper
scraper = LinkedinScraper(
    chrome_executable_path=None,
    chrome_binary_location=None,
    chrome_options=None,
    headless=True,
    max_workers=10,
    slow_mo=1.3,  # Increase the delay between requests
    page_load_timeout=5000  # Increase timeout to 5000 milliseconds (5 seconds)
)

# Add event listeners
scraper.on(Events.DATA, on_data)
scraper.on(Events.ERROR, on_error)
scraper.on(Events.END, on_end)

# Define the query with updated filters
query = Query(
    query='data science',
    options=QueryOptions(
        locations=['Ahmedabad'],
        apply_link=True,
        skip_promoted_jobs=True,
        limit=100,
    )
)

@retry(stop_max_attempt_number=2, wait_fixed=10000)
def run_scraper():
    """Run the scraper with retry logic and track execution time."""
    start_time = time.time()  # Record the start time
    try:
        logging.info('Starting scraper...')
        scraper.run([query])
        logging.info('Scraper finished successfully.')
    except Exception as e:
        logging.error(f"Error running scraper: {e}")
        raise
    finally:
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time
        logging.info(f"Total execution time: {execution_time:.2f} seconds")

run_scraper()
