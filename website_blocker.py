import time
from datetime import datetime as dt

hosts_path = r'/private/etc/hosts'
hosts_temp = 'hosts'
redirect = '127.0.0.1'
websites_list = ['www.facebook.com', 'www.instagram.com', 'facebook.com', 'instagram.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("work hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        print("non work hours")
    time.sleep(5)
