import requests
from bs4 import BeautifulSoup
import re


if __name__ == "__main__":
    r = requests.get("http://mag234.com/index/index")
    r.raise_for_status()
    html = r.text
    #print(html)
    #matches = re.findall(r"\圓\d+", html)
    #print(matches)
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('li')
    #print(links)
    for link in links:
        #print('id:"{}"'.format(link.attrs['data-id']))
        #print('magnet:"{}"'.format(link.attrs['data-magnet']))
        print('ed2k:"{}"'.format(link.attrs['data-ed2k']))




