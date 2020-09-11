'Definition and Usage:'
->The requests module allows you to send HTTP requests using Python.
->The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

'Syntax'
requests.methodname(params)

#Methods
'Method'	                                        'Description'
delete(url, args)	        Sends a DELETE request to the specified url
get(url, params, args)	        Sends a GET request to the specified url
head(url, args)	                Sends a HEAD request to the specified url
patch(url, data, args)	        Sends a PATCH request to the specified url
post(url, data, json, args)	Sends a POST request to the specified url
put(url, data, args)	        Sends a PUT request to the specified url
request(method, url, args)	Sends a request of the specified method to the specified url



#Parameter Values of Requests

'Parameter'		    'Description'
url		        Required. The url of the request

params		        Optional. A dictionary, list of tuples or bytes to send as a query string.
                        Default None

allow_redirects		Optional. A Boolean to enable/disable redirection.
                        Default True (allowing redirects)

auth		        Optional. A tuple to enable a certain HTTP authentication.
                        Default None

cert		        Optional. A String or Tuple specifying a cert file or key.
                        Default None

cookies		        Optional. A dictionary of cookies to send to the specified url.
                        Default None

headers		        Optional. A dictionary of HTTP headers to send to the specified url.
                        Default None

proxies		        Optional. A dictionary of the protocol to the proxy url.
                        Default None

stream		        Optional. A Boolean indication if the response should be immediately downloaded (False) or streamed (True).
                        Default False

timeout		        Optional. A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.
                        Default None which means the request will continue until the connection is closed

verify	                Optional. A Boolean or a String indication to verify the servers TLS certificate or not.
                        Default True
