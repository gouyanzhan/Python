import both as both
import requests
from are import are

s = requests.Session()
s.auth = ('user','pass')
s.headers.update({'x-test':'true'})

# both 'x-test' and 'x-test2' are sent
s.get('http://httpbin.org/headers',headers ={'x-test2':'true'})

