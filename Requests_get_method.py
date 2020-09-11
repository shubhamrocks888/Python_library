                    ##GET REQUEST

'Definition and Usage'
The get() method sends a GET request to the specified url.

'Syntax:'
->requests.get(url, params={key: value}, args)
->args means zero or more of the named arguments in the parameter table below. Example:

->requests.get(url, timeout=2.50)

##Example:
import requests

response = requests.get('https://w3schools.com')
print (response)
#Output: <Response [200]>

#Invalid url
response = requests.get('https://w3schools.com/monty')
print (response)
#Output: <Response [404]>

##Example:
import requests

url = 'https://httpbin.org/get'
x = requests.get(url)

print (x.text)
#Output: Response Body
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.24.0", 
    "X-Amzn-Trace-Id": "Root=1-5f5bb87b-86797dfe5e2f7360312cf004"
  }, 
  "origin": "106.207.249.64", 
  "url": "https://httpbin.org/get"
}

print (type(x.text))
#Output: <class 'str'>

print (x.json())

{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org',
                         'User-Agent': 'python-requests/2.24.0', 'X-Amzn-Trace-Id': 'Root=1-5f5bb8f9-a7ef8800f6badc02a343a30f'},
 'origin': '106.207.249.64', 'url': 'https://httpbin.org/get'}

print (type(x.json()))
#Output: <class 'dict'>

print (x.json['url'])
#Output: https://httpbin.org/get

print (x.headers)
#Output: Response headers

{'Date': 'Fri, 11 Sep 2020 17:59:18 GMT', 'Content-Type': 'application/json', 'Content-Length': '306', 'Connection': 'keep-alive',
 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}

##Example:
import requests

url = 'https://httpbin.org/get'
payload = {'page':2}

x = requests.get(url,params=payload)

print (x.url)
#Output: https://httpbin.org/get?page=2



                    
