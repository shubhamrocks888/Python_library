                    ##POST REQUEST

'Definition and Usage':
->The post() method sends a POST request to the specified url.

->The post() method is used when you want to send some data to the server.

'Syntax':
-> requests.post(url, data={key: value}, json={key: value}, args)
-> args means zero or more of the named arguments in the parameter table below. Example:

requests.post(url, data = myobj, timeout=2.50)

####
import requests

url = 'https://httpbin.org/post'
payload = {'username':'monty','password':123456,}

x = requests.post(url,data=payload)

print (x.text)

#Output:
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "password": "123456", 
    "username": "monty"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "30", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.24.0", 
    "X-Amzn-Trace-Id": "Root=1-5f5bc51b-9484a110a2321380535711b0"
  }, 
  "json": null, 
  "origin": "27.56.195.52", 
  "url": "https://httpbin.org/post"
}
