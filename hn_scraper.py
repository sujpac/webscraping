import requests
from bs4 import BeautifulSoup
import json

scraping_hn = True
page = 1
output = []

print("Starting Hacker News Scraper...")

while scraping_hn:
    response = requests.get(f"https://news.ycombinator.com/?p={page}")
    html = response.text

    print(f"Scraping {response.url}")

    # Parse the html
    soup = BeautifulSoup(html, features="html.parser")
    articles = soup.find_all(class_="athing")

    for article in articles:
        data = {
            "URL": article.find(class_="titleline").find("a").get("href"),
            "title": article.find(class_="titleline").getText(),
            "rank": article.find(class_="rank").getText().replace(".", "")
        }
        output.append(data)

    # Check if scraper reached the last page
    next_page = soup.find(class_="morelink")

    if next_page is not None:
        page += 1
    else:
        scraping_hn = False
        print(f"Finished scraping! Scraped {len(output)} items.")

print("Saving output data to JSON file.")
save_output = open("hn_data.json", "w")
json.dump(output, save_output, indent=6, ensure_ascii=False)
save_output.close()
