import browser as b

from selenium import webdriver as wd
from selenium import selenium


BTSurl="http://www.transtats.bts.gov/\
DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time"

#table with fields xpath: this is the table in the page that contains
#all the variables. i got this by inspecting code on chrome
fields_tbl_xpth='//*[@id="content"]/table[1]/tbody/tr/td[2]/table[4]'
#table that has the filters
filters_tbl_xpth='//*[@id="content"]/table[1]/tbody/tr/td[2]/table[2]'


def get_browser(*args,**kwargs):
    browser=b.get_browser(*args,**kwargs)
    browser.get(BTSurl)
    return browser

def init(*args,**kwargs):
    global browser #sinner!
    browser=get_browser(*args,**kwargs)
    global fields_tbl
    fields_tbl=browser.find_element_by_xpath(fields_tbl_xpth)

from selenium.webdriver.support.select import Select

#all Variable have VarName in the name attrib

#todo get variables
#todo get filters: geo, yr, and period

#the titles give the variable names
def get_varElems():
    """gets the fields elements checkboxes.
    they are all: class=checkbox, name=VarName, id=VarName"""
    return fields_tbl.find_elements_by_name("VarName")
#title attrib shows up in the page and value attriib shows in the csv

#utils
def up1(elem): return elem.find_element_by_xpath('..')
def up(elem,by=1):
    for i in xrange(by):
        elem=up1(elem)
    return elem


def get_Description(chkboxElem):
    cb = chkboxElem
    r = up(cb,by=2)
    d= r.find_elements_by_class_name('dataTD')[1] #the second one
    return d.text

def get_lookupTblElem(chkboxElem):
    """go up the hierarchy two levels to get to table row,
    then find look up link
    you get NoSuchElemException if no lookup link"""
    cb = chkboxElem
    r = up(cb,by=2)#cb.find_element_by_xpath('../..')
    link = r.find_element_by_partial_link_text('Lookup')
    return link #you get NoSuchElementException if there is no lookup tbl

def get_filterElems():pass
    
    
def download(geo,yr,mo):pass

#todo set download dir in config
