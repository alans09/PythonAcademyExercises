import requests

res = requests.get("https://www.root.cz")
print(res.text)
