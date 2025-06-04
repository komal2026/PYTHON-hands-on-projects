import requests
query =input("What type of news  you interested in today?")
api = "e2b842b7b4d8412aa2ceaf28de38aae4"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-04&sortBy=publishedAt&apiKey={api}"
print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1 ,article["title"], article["urlToImage"], article["url"])
    print("\n*************************************\n")
