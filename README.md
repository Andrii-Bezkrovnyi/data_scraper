# Data Scraper

This repository contains scripts to scrape data from restcountries.com and ebay.com page and store it in JSON and CSV files. Scripts uses Selenium for web scraping and supports scraping intervals.

## How Setup and Execution code

### 1. Set Up the Scraping Environment

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Andrii-Bezkrovnyi/data_scraper.git
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate (on Windows) 
    source venv/bin/activate  (on Linux)
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Execute the Script for the site restcountries.com**

    ```sh
     python country_api.py
    ```
This script connect to the api of the site restcountries.com,download data  about countries from this site and create a file  `countries.csv` with this data.

5. **Execute the Script for the site ebay.com**

    ```sh
     python ebay_scraper.py
    ```
   This script will start the scraping and create a file  `product_data.json` with the scraped data about one product from the site ebay.com.
