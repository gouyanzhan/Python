import requests

response = requests.get('https://api.github.com/events')
Response = requests.post('http://httpbin.org/post', data = {'key':'value'})
Response = requests.put('http://httpbin.org/put', data = {'key':'value'})
Response = requests.delete('http://httpbin.org/delete')
Response = requests.head('http://httpbin.org/get')
Response = requests.options('http://httpbin.org/get')