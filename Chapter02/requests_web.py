import requests

if __name__ == '__main__':
    r = requests.get("https://shanghai.craigslist.org/")
    print(r.headers['content-type'])
    print(r.content[:1000])


