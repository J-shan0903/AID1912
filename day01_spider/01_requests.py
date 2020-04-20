

import requests
response = requests.get(url='https://www.jd.com/')
# html = response.text
# content = response.content
# status_code = response.status_code
url = response.url
print(url)




