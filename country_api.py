import pandas as pd
import requests
from tqdm import tqdm


class CountryAPI:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.ok:
            return response.json()
        else:
            response.raise_for_status()

    def get_country_info(self):
        data = self.fetch_data()
        countries = []
        for country in tqdm(data, desc="Loading data"):
            name = country.get('name', {}).get('common', 'N/A')
            capital = country.get('capital', ['N/A'])[0]
            flags = country.get('flags', [])
            flag_url = flags[1] if len(flags) > 1 else 'N/A'
            countries.append({
                'Country': name,
                'Capital': capital,
                'Flag': flag_url
            })
        return countries

    def save_to_csv(self, filename='countries.csv'):
        country_info = self.get_country_info()
        df = pd.DataFrame(country_info)
        df.to_csv(filename, index=False)
        print(f"Data has been saved to {filename}")


if __name__ == "__main__":
    api_url = "https://restcountries.com/v3/all"
    country_api = CountryAPI(api_url)
    country_api.save_to_csv()
