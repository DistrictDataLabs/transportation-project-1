browsers=['chrome','firefox','ie']
browser_drivers=dict.fromkeys(browsers)
default_browser='chrome'

#todo make use of default dict

import resources as resrcs

import os
#add/change your driver here
browser_drivers['chrome']=os.path.join(resrcs.dirs['data_store']
                        ,'data/scraped/drivers/chromedriverw32.exe')

#todo see if there is a portable way to specify this. this is ugly!
#or at least a way to 'push' a dir to the browser
browser_download_dir=r'C:\Users\Majid\Downloads'

extract_to=os.path.join(resrcs.dirs['data_store']
                    ,'data/scraped/bts')

