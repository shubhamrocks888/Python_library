'Definition and Usage:'
->The requests.Response() Object contains the servers response to the HTTP request.


#Properties and Methods

'Property/Method'		'Description'
apparent_encoding		Returns the apparent encoding
close()		                Closes the connection to the server
content		                Returns the content of the response, in bytes
cookies		                Returns a CookieJar object with the cookies sent back from the server
elapsed		                Returns a timedelta object with the time elapsed from sending the request to the arrival of the response
encoding		        Returns the encoding used to decode r.text
headers		                Returns a dictionary of response headers
history		                Returns a list of response objects holding the history of request (url)
is_permanent_redirect		Returns True if the response is the permanent redirected url, otherwise False
is_redirect		        Returns True if the response was redirected, otherwise False
iter_content()		        Iterates over the response
iter_lines()		        Iterates over the lines of the response
json()		                Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
links		                Returns the header links
next		                Returns a PreparedRequest object for the next request in a redirection
ok		                Returns True if status_code is less than 200, otherwise False
raise_for_status()		If an error occur, this method returns a HTTPError object
reason		                Returns a text corresponding to the status code
request		                Returns the request object that requested this response
status_code		        Returns a number that indicates the status (200 is OK, 404 is Not Found)
text		                Returns the content of the response, in unicode(string)
url		                Returns the URL of the response


1.                  'status_code'

x = requests.get('http://google.com')
print (x.status_code)

#Output: 200


2.                  'url'

x = requests.get('http://wikipedia.org')

#print the url that we get in response:
print(x.url)

#Output:
https://www.wikipedia.org/


3.                  'text'

x = requests.get('https://w3schools.com/python/demopage.htm')

#print the response text (the content of the requested file):
print(x.text)

#Output:
C:\Users\My Name>python demo_requests_get_url.py
<!DOCTYPE html>

<html>
<body>

<h1>This is a Test Page</h1>

</body>
</html>

print (type(x.text))
#Output: <class 'str'>


4.                  'params'

#PARAMETERS          #DESCRIPTION         
params		 A dictionary, list of tuples or bytes to send as a query string.
                 Default None

url = 'https://www.w3schools.com/python/showpython.asp'

#demonstrate how to use the 'params' parameter:
x = requests.get(url, params = {"filename": "demo_requests_get_params"})

print(x.url)
#Output: https://www.w3schools.com/python/showpython.asp?filename=demo_requests_get_params

print (x.text)
# Response is of 615 lines:

<!DOCTYPE html>

<html lang="en-US">

<head>

<title>Tryit Editor v3.6 - Show Python</title>

<meta name="viewport" content="width=device-width">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<link rel="stylesheet" href="/w3css/4/w3.css">

<link rel="stylesheet" href="/lib/codemirror.css">

.................
</script>

</body>

</html>


#NOTE:
https://www.w3schools.com/python/showpython.asp?filename=demo_requests_get_params
->After ?,there is a param parameter


5.                  'allow_redirects'

#PARAMETERS             #DESCRIPTION
allow_redirects		Optional. A Boolean to enable/disable redirection.
                        Default True (allowing redirects)

#to demonstrate the 'allow_redirects' parameter we use 'http' instead of 'https',w3schools.com automatically redirects http requests to https:
url = 'http://w3schools.com/python/demopage.htm'

#first, make a request without setting the 'allow_redirects' parameter to False:
x = requests.get(url)
print(x.text)

print("----------------")

print (x.url)

print("----------------")

#then, make a request with the 'allow_redirects' parameter set to False:
x = requests.get(url, allow_redirects=False)
print(x.text)

#Output:
<!DOCTYPE html>

<html>

<body>



<h1>This is a Test Page</h1>



</body>

</html>
----------------
https://www.w3schools.com/python/demopage.htm
----------------
<head><title>Document Moved</title></head>
<body><h1>Object Moved</h1>This document may be found <a HREF="https://www.w3schools.com/python/demopage.htm">here</a></body>


6.                  'auth'

#PARAMETERS     #DESCRIPTION
auth		Optional. A tuple to enable a certain HTTP authentication.
                Default None


url = 'https://w3schools.com/python/demopage.php'

#use the 'auth' parameter to send requests with HTTP Basic Auth:
x = requests.get(url, auth = ('user', 'pass'))

print(x.status_code)
#Output: 200


7.                  'cookies'

#PARAMETERS     #DESCRIPTION
cookies		Optional. A dictionary of cookies to send to the specified url.
                Default None

url = 'https://w3schools.com/python/demopage2.php'

#use the 'cookies' parameter to send cookies to the server:
x = requests.get(url, cookies = {"favcolor": "Red"})

print(x.text)
#the 'demopage2.php' prints the value of the 'favcolor' cookie.

<!DOCTYPE html>
<html>
<body>

<p>Favorite color: Red</p>

</body>
</html>


8.                  'headers'

#PARAMETERS     #DESCRIPTION
headers		Optional. A dictionary of HTTP headers to send to the specified url.
                Default None

url = 'https://w3schools.com/python/demopage.asp'

#use the 'headers' parameter to set the HTTP headers:
x = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})

print(x.text)

#the 'demopage.asp' prints all HTTP Headers
HTTP_CONNECTION:keep-alive
HTTP_ACCEPT:*/*
HTTP_ACCEPT_ENCODING:gzip, deflate
HTTP_HOST:MyVeryOwnHost
HTTP_USER_AGENT:python-requests/2.22.0


9.                  'reason'
import requests

url = 'https://www.w3schools.com/python/demopage.htm'
x = requests.get(url)
print(x.reason)
#Output: OK

##for false url
x = requests.get('https://www.w3schools.com/python/demopage.htm/monty')
print (x.reason)
#Output: Not Found


10.                 'request'
import requests

url = 'https://www.w3schools.com/python/demopage.htm'
x = requests.get(url)

print(x.request)
#Output: <PreparedRequest [GET]>


11.             'raise_for_status'
import requests

#enter a wrong url:
url = 'https://www.w3schools.com/python/demopagdddddd.htm'

x = requests.get(url)
print(x.raise_for_status())

#Output: requests.exceptions.HTTPError: 404 Client Error

#for right url:
x = requests.get('https://www.w3schools.com')
print (x.raise_for_status())

#Output: None


12.                     'next'
import requests

url = 'https://www.youtube.com/channel/UCt4t-jeY85JegMlZ-E5UWtA'

x = requests.get(url)

print(x.next)
#Output: None


13.                     'json'
import requests

url = 'https://www.w3schools.com/python/demopage.js'

x = requests.get(url)

print(x.json())
#Output: {'firstname':'John','lastname':'Doe'}

print (type(x.json()))
#Output: <class 'dict'>

print(x.json()['firstname'])
#Output: John


                      







