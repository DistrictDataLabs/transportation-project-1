browsers=['chrome','firefox','ie']
browser_drivers=dict.fromkeys(browsers)
default_browser='chrome'

#add/change your driver here
browser_drivers['chrome']=r'c:\users\majid\desktop\chromedriver.exe'

browser_download_dir='C:\Users\Majid\Downloads'
extract_to='C:\Users\Majid\Dropbox\Transportation\data'

import os
download_dir=os.curdir
