import requests
from lxml import html
USERNAME = "B20DCAT206"
PASSWORD = "10052002"

LOGIN_URL = "https://www.code.ptit.edu.vn"

def main():
    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    payload = {
        "userid": USERNAME, 
        "password": PASSWORD,
        "submit":"Login"
    }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL)).text
    # tree = html.fromstring(result.content)

    print(result)

if __name__ == '__main__':
    main()