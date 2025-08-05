import os
import requests
from datetime import datetime
import random

# Get today's date
today = datetime.now()
month = today.month
day = today.day
date_str = today.strftime("%Y-%m-%d")
pretty_date = today.strftime("%B %d")

# Create history folder if it doesn't exist
if not os.path.exists("history"):
    os.makedirs("history")

# API URL
url = f"https://history.muffinlabs.com/date/{month}/{day}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    events = data["data"]["Events"]
    selected_events = random.sample(events, 3)

    md_content = f"# Today in History - {pretty_date}\n\n"
    for i, event in enumerate(selected_events, 1):
        year = event["year"]
        text = event["text"]
        md_content += f"## Event {i}\n📅 Year: {year}  \n📝 Event: {text}\n\n"

    file_path = f"history/{date_str}.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"History for today saved to {file_path}")
else:
    print("Failed to fetch historical data.") 