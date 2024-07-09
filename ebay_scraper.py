import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class EbayScraper:
    def __init__(self, url: str):
        """
        Initializes the EbayScraper class with the given URL.

        Args:
            url (str): The URL of the eBay product page.
        """
        self.url = url
        self.data: dict[str, str] = {}

    def fetch_page(self) -> None:
        """
        Fetches the eBay product page using Selenium with a headless Chrome browser.
        """
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get(self.url)
        time.sleep(3)  # Wait for the page to load

    def parse_page(self) -> None:
        """
        Parses the eBay product page to extract required information.
        """
        # Extract product name
        try:
            product_name = self.driver.find_element(By.CSS_SELECTOR, '.vim.x-item-title > h1')
            self.data['product_name'] = product_name.text.strip()
        except:
            self.data['product_name'] = 'N/A'
            print("Product name not found")

        self.data['product_url'] = self.url

        # Extract photo URL
        try:
            photo_url = self.driver.find_element(By.CSS_SELECTOR, '.image-treatment.active.image > img')
            self.data['photo_url'] = photo_url.get_attribute('src')
        except:
            self.data['photo_url'] = 'N/A'
            print("Photo URL not found")

        # Extract price
        try:
            price = self.driver.find_element(By.CSS_SELECTOR, '.x-price-primary')
            self.data['price'] = price.text.strip()
        except:
            self.data['price'] = 'N/A'
            print("Price not found")

        # Extract seller information
        try:
            seller = self.driver.find_element(By.CSS_SELECTOR,
                                              '.d-stores-info-categories__container__info__section h2 a span')
            self.data['seller'] = seller.text.strip()
        except:
            self.data['seller'] = 'N/A'
            print("Seller not found")

        # Extract shipping cost
        try:
            shipping_info = self.driver.find_element(By.CSS_SELECTOR,
                                                     '.ux-labels-values__values.col-9 span.ux-textspans--BOLD.ux-textspans')
            self.data['shipping_cost'] = shipping_info.text.strip()
        except:
            self.data['shipping_cost'] = 'N/A'
            print("Shipping cost not found")

    def save_to_json(self, filename: str = 'product_data.json') -> None:
        """
        Saves the extracted data to a JSON file.

        Args:
            filename (str): The name of the JSON file. Defaults to 'product_data.json'.
        """
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"Data has been saved to {filename}")

    def display_data(self) -> None:
        """
        Displays the extracted data in JSON format.
        """
        print(json.dumps(self.data, indent=4))

    def scrape(self) -> None:
        """
        Orchestrates the scraping process by fetching the page, parsing the data, and displaying it.
        """
        self.fetch_page()
        self.parse_page()
        self.display_data()
        self.driver.quit()


if __name__ == "__main__":
    url = "https://www.ebay.com/itm/275923774946"
    scraper = EbayScraper(url)
    scraper.scrape()
    scraper.save_to_json()
