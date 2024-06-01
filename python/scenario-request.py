import requests
import json
import time

base_url = "https://kovaaks.com/webapp-backend/scenario/popular"
headers = {
    'Authorization': 'Bearer' # No need for token auth
}

all_data = []
total_scenarios = 10000
items_per_page = 20
total_pages = (total_scenarios - 1) // items_per_page + 1
retry_delay = 5

for page in range(1, total_pages + 1):
    api_url = f"{base_url}?page={page}&max={items_per_page}"

    while True:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            all_data.extend(data["data"])

            if len(all_data) >= total_scenarios:
                all_data = all_data[:total_scenarios]
                break 
            break 
        elif response.status_code == 429:
            print(f"Rate limited on page {page}, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print(f"Error fetching page {page}: {response.status_code}")
            break

with open("top_10k_scenarios.json", "w") as outfile:
    json.dump(all_data, outfile)
