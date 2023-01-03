import json
import requests
from requests.exceptions import HTTPError

"""
To send https api request in python, we can use requests library. It is not
a python built module so first we need to install it using pip.
pip install requests
and then import it using import requests.

Requests will automatically decode content from the server. Most unicode
charsets are seamlessly decoded.

When you make a request, Requests makes educated guesses about the encoding
of the response based on the HTTP headers. The text encoding guessed by
Requests is used when you access r.text. You can find out what encoding
Requests is using, and change it, using the response.encoding property:

response.encoding
'utf-8'
response.encoding = 'ISO-8859-1'
response.text
If you change the encoding, Requests will use the new value of
response.encoding whenever you call response.text.
"""
print("----------------Example 1---------------------")
response = requests.get('https://api.github.com')
print(response.status_code)

try:
    response = requests.get("https://api.github.com")
    # If the status code
    # indicates a successful request, the program will proceed without any
    # exception being raised. If an HTTP error occurs (e.g. a 4xx or 5xx status
    # code), the HTTPError exception will be raised. If any other exception
    # occurs, the Exception exception will be raised.
    response.raise_for_status()
except HTTPError as httpError:
    print(f"Http error occurred {httpError}")
except Exception as err:
    print(f"Some other exception occurred {err}")
else:
    print(response.status_code)  # Response status code
    print(response.encoding)
    print(response.text)  # response in string format

    # one way to get response in python dictionary format
    text = response.text
    resInPythonFormat = json.loads(text)
    print(resInPythonFormat)

    # Another easier way to get response in python dictionary format
    resInPythonDictionary = response.json()
    print(resInPythonDictionary)

    # response headers
    print(response.headers)
    print(response.headers['content-type'])

print("---------------Example 2-------------------")
# Query params can be passed as python dictionary or list of tuples using a
# parameter called params.
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

print("------------Example 3----------------")
# To customize headers, you pass a dictionary of HTTP headers to get() using
# a parameter called headers.
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
"""
The Request Body:
According to the HTTP specification, POST, PUT, and the less common PATCH
requests pass their data through the message body. To do this we use a
parameter named data while sending request.

data takes a dictionary, a list of tuples, bytes, or a file-like object.

if your request’s content type is application/x-www-form-urlencoded,
you can send the form data as a dictionary.
"""
print("------------Example 4----------------")
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)

"""
There are times that you may want to send data that is not form-encoded. If you
pass in a string instead of a dict, that data will be posted directly.
"""
print("------------Example 5----------------")
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print(r.text)

"""
Please note that the above code will NOT add the Content-Type header
(so in particular it will NOT set it to application/json). If you need that
header set and you don’t want to encode the dict yourself, you can also pass it
directly using the json parameter (added in version 2.4.2) and it will be
encoded automatically
"""
print("------------Example 6----------------")
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
r = requests.post(url, json=payload)

"""
Cookies: To send your own cookies to the server, you can use the cookies
parameter.
"""
print("------------Example 7----------------")
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r1 = requests.get(url, cookies=cookies)
print(r1.text)

"""
If a response contains some Cookies, you can quickly access them:
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)

r.cookies['example_cookie_name']
"""

"""
Inspecting Your Request
When you make a request, the requests library prepares the request before
actually sending it to the destination server. Request preparation includes
things like validating headers and serializing JSON content.

You can view the PreparedRequest by accessing .request
"""
print("------------Example 8----------------")
response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.request.headers['Content-Type'])
print(response.request.url)
print(response.request.body)

# SSL Certificate Verification: verifying the target server’s SSL Certificate
# If you want to disable SSL Certificate verification, you pass False to the
# verify parameter of the request function.
requests.get('https://api.github.com', verify=False)

"""
Client Side Certificates
You can also specify a local cert to use as client side certificate,
as a single file (containing the private key and the certificate) or as a
tuple of both files’ paths:

requests.get('https://kennethreitz.org', cert=('client.cert',
'/path/client.key'))
"""
