# LinkedIn Job Extractor

A Python script for scraping job listings from LinkedIn using the `linkedin_jobs_scraper` library. This script extracts job data based on specified queries and filters, processes the data, and saves it to an CSV file.

## Features

- Scrapes job listings from LinkedIn based on predefined queries and filters.
- Handles errors with retry logic and logs detailed information.
- Saves the collected job data to an CSV file.
- Supports custom directory paths for saving the CSV file.

![App Screenshot](https://github.com/priyanshurathod009/LinkJobExtract-Tool/blob/main/Image/Image02.png?raw=true)

## Requirements

- Python 3.8+
- `pandas`
- `selenium`
- `linkedin_jobs_scraper`
- `retrying`

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/priyanshurathod009/LinkJobExtract-Tool.git
    cd LinkJobExtract-Tool
    ```

2. **Install the required packages**:
    ```bash
    pip install pandas selenium linkedin_jobs_scraper retrying
    ```

## Configuration

1. **Set up environment variables**:
    - Define the `JOB_DATA_DIR` environment variable for the directory where the Excel file will be saved. If not set, it defaults to `C:/Users/priyanshu/`.

2. **Adjust script parameters**:
    - Modify the `query` object in the script to change the job search parameters.

## Usage

1. **Run the script**:
    ```bash
    python your_script_name.py
    ```

2. **Script Details**:
    - **`on_data`**: Processes and logs job data.
    - **`on_metrics`**: Handles metrics data with a sleep interval.
    - **`on_error`**: Handles errors and retries if necessary.
    - **`on_end`**: Saves the collected data to an Excel file.
    - **`wait_for_element`**: Waits for an element to be present on the page.
    - **`run_scraper`**: Runs the scraper with retry logic and tracks execution time.

## Example

The script is configured to search for `Data Analyst` jobs in specific locations, including `Indore, Jaipur, Pune, Ahmedabad and Noida`. It skips promoted jobs and limits the results to 100.

## Logging

The script uses Python's `logging` module to log information, warnings, and errors. Log messages are output to the console and include timestamps and log levels.

## Error Handling

The script includes exception handling for common errors, such as JavaScript and timeout errors, with retry logic to manage intermittent issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact:

For inquiries or further information, please contact

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/priyanshu-rathod/)
