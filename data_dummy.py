import pandas as pd
import numpy as np
import random
from faker import Faker
#Esta libreria  Faker nos ayudara a sintetizar data 
faker = Faker()

# Parameters for dates
start_date = pd.to_datetime("2024-01-01")
end_date = pd.to_datetime("2024-12-31")
dates = pd.date_range(start=start_date, end=end_date)
# Social media to create some data
sources = [
    "Facebook", "Google Ads", "LinkedIn Ads", "TikTok Ads", "Twitter",
    "Instagram Organic", "Reddit", "Snapchat Ads", "YouTube Organic", "Capterra"
]
# Any social media have chanels to publish campaings
channels = {
    "Facebook": "Paid Social",
    "Google Ads": "Paid Search",
    "LinkedIn Ads": "Paid Social",
    "TikTok Ads": "Paid Social",
    "Twitter": "Paid Social",
    "Instagram Organic": "Organic",
    "Reddit": "Programmatic",
    "Snapchat Ads": "Paid Social",
    "YouTube Organic": "Organic",
    "Capterra": "Programmatic"
}

campaigns = [f"Campaign {i}" for i in range(1, 21)]

# Asing campanins  for source
source_campaign_map = {
    source: random.sample(campaigns, k=random.randint(2, 6)) for source in sources
}

# Generate data random
rows = []
for date in dates:
    for source in sources:
        for campaign in source_campaign_map[source]:
            #IMpressions could be around 1000 an 100000
            impressions = np.random.randint(1000, 100000)
            clicks = np.random.randint(50, impressions // 5)
            conversions = np.random.randint(5, clicks // 2 + 1)
            cost = round(np.random.uniform(20, 5000), 2)
            revenue = round(cost * np.random.uniform(1.1, 3.5), 2)

            row = {
                "Date": date,
                "Channel": channels[source],
                "Impresions": impressions,
                "Clicks": clicks,
                "CTR": round(clicks / impressions, 4),
                "Conversions": conversions,
                "Cost": cost,
                "Revenue": revenue,
                "Source": source,
                "CPM": round((cost / impressions) * 1000, 2),
                "CPC": round(cost / clicks, 2),
                "ROAS": round(revenue / cost, 2),
                "SPEND": cost,
                "campaign_name": campaign
            }
            rows.append(row)


df = pd.DataFrame(rows)

print(df.head())
# For all the year this is the data saved
file_path = "campaign_performance_dummy_full_year.csv"
df.to_csv(file_path, index=False)

print(f"Archivo guardado en: {file_path}")