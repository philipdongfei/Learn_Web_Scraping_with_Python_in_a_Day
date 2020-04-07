import requests
import re


if __name__ == "__main__":
    r = requests.get("https://shanghai.craigslist.org/search/hhh?query=apartment&sort=rel&lang=en&cc=us")
    r.raise_for_status()
    html = r.text

    #matches = re.findall(r"\圓\d+", html)
    #print(matches)
    matches = re.findall(r'<span class="result-price">\圓(\d+)</span>', html)
    '''

    for i in matches:
        if len(i) == 1:
            print(i)
    '''
    prices = list(map(int, matches))
    print("Highest price: yuan{}".format(max(prices)))
    print("Lowest price: yuan{}".format(min(prices)))
    print("Average price: yuan{}".format(sum(prices)/len(prices)))


