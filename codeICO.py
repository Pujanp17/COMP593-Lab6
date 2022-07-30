import requests

url = "https://www.ontario.ca//base/images/favicon.ico"
r = requests.get(url, allow_redirects=True)

open('Ontario.ico', 'wb').write(r.content)