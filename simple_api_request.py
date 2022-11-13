# import requests

# req = request.get("https://google.com")
# print(req.status_code)


import requests
import time
while True:
    req = requests.get("website.com")
    print(req.status_code)
    if req.status_code != 200:
        #email me or text me
        pass
    time.sleep(60)


    # an uptime monitoring program to check whether a site is online! 