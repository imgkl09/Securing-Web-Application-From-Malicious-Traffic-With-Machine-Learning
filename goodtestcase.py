import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

data = {
    'username': 'exampleuser',
    'password': 'examplepassword'
}

url = 'http://localhost:3000'

response = requests.post(url, headers=headers, data=data, verify=False)

print(response.status_code)
print(response.text)
