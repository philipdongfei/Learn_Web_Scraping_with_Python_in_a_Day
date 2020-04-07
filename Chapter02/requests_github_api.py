import requests

if __name__ == '__main__':
    r = requests.get('https://api.github.com', auth=('philip.dongfei@gmail.com', 'Sting1979416'))
    if r.ok:
        print(r.text)
    else:
        print("Something went wrong:{}".format(r.reason))
    print(r.status_code)
    if r.status_code == requests.codes.OK:
        print("Everything worked!")
    elif r.status_code == requests.codes.BAD:
        print("Something went wrong!")
    elif r.status_code == requests.codes.NOT_FOUND:
        print("The server couldn't find this URL!")
    elif r.status_code == requests.codes.NOT_ALLOWED:
        print("You aren't allowed to access this!")
    else:
        print("Something else happened: {}".format(r.reason))
    print(requests.codes["MOVED"] == 301)
    print(requests.codes.request_timeout == requests.codes.REQUEST_TIMEOUT)
    print(r.headers['content-type'])

    print()

    r = requests.get('https://github.com/timeline.json')
    print("Status code: {} '{}'".format(r.status_code, r.reason))
    print(r.headers['content-type'])
    print(r.text)
    print(r.json()['message'])


