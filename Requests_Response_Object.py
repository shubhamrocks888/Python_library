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
text		                Returns the content of the response, in unicode
url		                Returns the URL of the response
