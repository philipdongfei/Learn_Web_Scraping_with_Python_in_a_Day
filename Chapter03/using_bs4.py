from bs4 import BeautifulSoup

if __name__ == '__main__':
    html_doc = '<a href="http://www.example1.com" id="link1">The first link!</a> <a id="link2" href="http://www.example2.com">The second link!</a>'
    soup = BeautifulSoup(html_doc, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        print('Link text:"{}"'.format(link.text))
        print('href:"{}"'.format(link.attrs['href']))
        print('id:"{}"\n'.format(link.attrs['id']))

