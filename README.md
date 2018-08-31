# Website Blocker

### This is a simple python script to block websites during your work hours, to not get distracted.

### Note

##### You can customize the work hours by changing the current work period(default  to 8AM to 4PM). This script will work only on **MAC/Linux**.
#
##### To make it work on Windows change the hosts_path to
#
```
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
```
##### To change the work hours
#
```
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day, 18):
```
##### Change this line to
#
```
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() \
            < dt(dt.now().year, dt.now().month, dt.now().day, 17):
```
##### If you want to change the work hours to 9AM to 5PM
#
##### To add websites to the block list, append the domain name of the website to this list which currently has instagram.com
#
```
websites_list = ['www.instagram.com', 'instagram.com']
```
### Get started(MAC/Linux)
#
```
sudo python website_blocker.py
```
##### To run the script as a crontab job
#
###### **Note** : You'll need to enter root password as the script edits the hosts file which needs permission
#
#
```
sudo crontab -e
```
###### To run the script everytime your machine reboots, edit the file(for **vim** enter i to edit, press escape and enter :wq to save and quit)
#
```
@reboot sudo python (your_filepath)/website_blocker.py
```
###### To delete the crontabs
#
```
sudo crontab -r
```

##### To learn more about crontab
#
###### MAC
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/QZJ1drMQz1A/0.jpg)](http://www.youtube.com/watch?v=QZJ1drMQz1A)
#
###### Linux
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/UlVqobmcPuM/0.jpg)](http://www.youtube.com/watch?v=UlVqobmcPuM)
#
###### Windows
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/sx4vh4KdFPw/0.jpg)](http://www.youtube.com/watch?v=sx4vh4KdFPw)




