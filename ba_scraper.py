import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Create an empty list to store reviews
all_reviews = []

# Step 2: Loop through the first 3 pages (you can increase it)
for page_num in range(1, 10):
    print(f"Scraping page {page_num}...")
    url = f"https://www.airlinequality.com/airline-reviews/british-airways/page/{page_num}/"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Step 3: Extract reviews from the page
    review_containers = soup.find_all("div", class_="text_content")

    for review in review_containers:
        review_text = review.get_text(strip=True)
        all_reviews.append(review_text)

    time.sleep(2)  # to avoid getting blocked

# Step 4: Save to CSV
df = pd.DataFrame(all_reviews, columns=["Review"])
df.to_csv("ba_reviews.csv", index=False)
print("✅ Scraping complete! Data saved to ba_reviews.csv")
