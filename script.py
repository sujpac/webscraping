import requests
response = requests.get("https://news.ycombinator.com/")
if response.status_code != 200:
    print("Error fetching page")
    exit()
else:
    content = response.content
print(content)
