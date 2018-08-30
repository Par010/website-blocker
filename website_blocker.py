import time
from datetime import datetime as dt
hosts_path = r'/private/etc/hosts'
redirect = '127.0.0.1'
websites_list = ['www.facebook.com', 'www.instagram.com', 'facebook.com', 'instagram.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("work hours")
    else:
        print("non work hours")
    time.sleep(5)
