import scrape_config
from selenium import webdriver as wd

def get_browser( browser_name = scrape_config.default_browser):
    """returns the selenium browser obj"""
    assert browser_name in scrape_config.browsers
    
    if browser_name is 'chrome':
        return wd.Chrome( scrape_config.browser_drivers[browser_name]  )
    #todo elif other browsers
    else: raise NotImplementedError

