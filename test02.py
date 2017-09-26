from urllib.request import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print(kittens[556:1000], "\n")
except(URLError, e):
    print('No kittez. Got an error code:', e)