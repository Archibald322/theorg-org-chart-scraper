"""
Apify Client Runner for The Org Org Chart & Decision Makers Scraper
Actor URL: https://apify.com/moneygain/theorg-org-chart-scraper
"""

import os
from apify_client import ApifyClient

# 1. Initialize the client with your Apify API token
# Get your free token at: https://console.apify.com/account/integrations
api_token = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
client = ApifyClient(api_token)

# 2. Define Actor input parameters
run_input = {
    "companySlugs": [
        "openai",
        "stripe"
    ],
    "maxMembersPerCompany": 25,
    "maxItems": 20,
    "proxyConfiguration": {
        "useApifyProxy": False
    }
}

def main():
    print("🚀 Starting The Org Org Chart & Decision Makers Scraper on Apify Cloud...")
    run = client.actor("moneygain/theorg-org-chart-scraper").call(run_input=run_input)
    print(f"✅ Scraping completed! Run ID: {run.get('id')}")
    
    # 3. Fetch results from default dataset
    dataset_client = client.dataset(run["defaultDatasetId"])
    items = list(dataset_client.iterate_items())
    print(f"📊 Retrieved {len(items)} decision maker records.")
    for item in items[:5]:
        print(f"• {item.get('fullName')} — {item.get('role')} at {item.get('companyName')} (Reports: {item.get('reportCount')})")

if __name__ == "__main__":
    main()
