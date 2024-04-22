

import requests

url = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos'
params ={'serviceKey' : 'nP48y1O6pt9zw6eUekNNCyiPVjqcECZPhaTgI49TzaXttCTKtRzhyBtVyZD//RVja9A5jf/lSMPEEeRN2KYOLA==', 'tmX' : '127.028', 'tmY' : '37.498', 'radius' : '300' }

response = requests.get(url, params=params)
print(response.content)