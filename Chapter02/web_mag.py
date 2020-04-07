import requests
import re


if __name__ == "__main__":
    r = requests.get("http://mag234.com/index/index")
    r.raise_for_status()
    html = r.text
    #print(html)
    #matches = re.findall(r"\圓\d+", html)
    #print(matches)
    '''

    matches = re.findall(r'data-magnet="(magnet:?[^\"]+)', html)
    for m in matches:
        print(m)
        print()
    '''
    matches = re.findall(r'data-ed2k="(ed2k:?[^\"]+)', html)
    for m in matches:
        print(m)
        print()


