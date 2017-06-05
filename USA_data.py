# import urllib, json
# url = "https://api.datausa.io/api/?show=geo&sumlevel=nation&required=pop"
# response = urllib.urlopen(url)
# print response
# data = json.loads(response.read())
# print data

import requests
r = requests.get('https://api.datausa.io/api/?show=geo&sumlevel=nation&required=pop')
print r.json()