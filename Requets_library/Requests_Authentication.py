                    ##Authentication using Python Requests
Authentication refers to giving a user permissions to access a particular resource.
Since, everyone can’t be allowed to access data from every URL, one would require authentication primarily.
To achieve this authentication, typically one provides authentication data through Authorization header or
a custom header defined by server.


# import requests module 
import requests 
from requests.auth import HTTPBasicAuth 

# Making a get request 
response = requests.get('https://api.github.com/user',auth = HTTPBasicAuth('shubhamrocks888','Monty@888')) 

#
print(response)
#Output: <Response [200]>
