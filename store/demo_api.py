

# import json
# import urllib.request

# url = urllib.request.urlopen(urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google"))
# data = json.loads(url.read().decode())  #load không s dùng sử lý dữ liệu cơ bản,loads dùng để xử lý dữ liệu phức tạp,dùng loads nhiều hơn load

# print(data)

# application/json trả
# text/json trả về 1 chuỗi json

import requests
import json

url_api = "https://fakestoreapi.com/products/1/"
#data = requests.get(url_api)
# data = json.loads(requests.get(url_api))
# print(data)
data = requests.get(url_api).json()
print(data)