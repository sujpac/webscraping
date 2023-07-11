import requests
from collections import Counter
from bs4 import BeautifulSoup
import json

response = requests.get("https://news.ycombinator.com/")
if response.status_code != 200:
    print("Error fetching page")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title)
print(soup.title.string)

num_links = len(soup.find_all('a'))
print(f"There are {num_links} links in this page")

first_link = soup.a
print(first_link)
print(first_link.get('href'))

pagespace = soup.find(id="pagespace")
print(pagespace)

athing = soup.find(class_="athing")
print(athing)

# Get the top 3 links
all_hrefs = [a.get('href') for a in soup.find_all('a')]
top3_links = Counter(all_hrefs).most_common(3)
print(top3_links)

# Extract only the article links from the main page
# NOTE: This doesn't work, there is no more "titlelink" class, find another
# way to grab just the article links


def my_tag_selector(tag):
    return tag.name == "a" and tag.has_attr("class") and "titlelink" in tag.get("class")


print(soup.find_all(my_tag_selector))

# Loop through each article and print its text contents to the
html = response.text
soup = BeautifulSoup(html)
articles = soup.find_all(class_='athing')

for article in articles:
    print(article.text)

# Extract each article's URL, title, and rank

output = []

for article in articles:
    data = {
        'URL': article.find(class_='titleline').find('a').get('href'),
        'title': article.find(class_='titleline').getText(),
        'rank': article.find(class_='rank').getText().replace('.', '')
    }
    output.append(data)

print(output)

print('Saving output data to JSON file.')
save_output = open('hn_data.json', 'w')
json.dump(output, save_output, indent=6, ensure_ascii=False)
save_output.close()
