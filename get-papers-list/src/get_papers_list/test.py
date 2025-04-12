import requests
print(requests.get("https://httpbin.org/get").status_code)