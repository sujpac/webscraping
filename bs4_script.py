import requests
from collections import Counter
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
if response.status_code != 200:
    print("Error fetching page")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title)

print(soup.title.string)

num_links = len(soup.find_all('a'))
print(f"There are {num_links} links in this page")

print(soup.get_text())

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


def my_tag_selector(tag):
    # TODO: This doesn't work, there is no more titlelink class, find another
    # way to grab just the article links
    return tag.name == "a" and tag.has_attr("class") and "titlelink" in tag.get("class")


print(soup.find_all(my_tag_selector))
