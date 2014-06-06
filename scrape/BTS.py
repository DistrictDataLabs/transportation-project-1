import browser as b

from selenium import selenium
from selenium.webdriver.support.select import Select

BTSurl="http://www.transtats.bts.gov/\
DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time"

#table with fields xpath: this is the table in the page that contains
#all the variables. i got this by inspecting code on chrome
fields_tbl_xpth= '//*[@id="content"]/table[1]/tbody/tr/td[2]/table[4]'
#table that has the filters
filters_tbl_xpth='//*[@id="content"]/table[1]/tbody/tr/td[2]/table[2]'
#the table that the downloadd button is in. it also has download options
#that i don't care about
dl_tbl_xpth='//*[@id="content"]/table[1]/tbody/tr/td[2]/table[3]'

def get_browser(*args,**kwargs):
    browser=b.get_browser(*args,**kwargs)
    browser.get(BTSurl)
    return browser

def init(*args,**kwargs):
    global browser #sinner!
    browser=get_browser()
    init_tbls()
    init_vars()
    init_filters()
    clearChkBoxes()
    selectFilterChoice('GEOGRAPHY','All ')


def clearChkBoxes():
    """doesn't get all of them"""
    clearVarSelections()
    clearZipDl()
    
def clearZipDl():
    ze=tbls['download'].find_element_by_name('DownloadZip')
    if ze.is_selected() is True:
        ze.click()

def init_tbls():
    fields_tbl=  browser.find_element_by_xpath(fields_tbl_xpth)
    filters_tbl= browser.find_element_by_xpath(filters_tbl_xpth)
    download_tbl=browser.find_element_by_xpath(dl_tbl_xpth)
    global tbls
    tbls= {'fields':fields_tbl
            ,'filters':filters_tbl
            ,'download':download_tbl}
    return tbls

def init_vars():
    global vars2elems
    ve=get_varElems()
    vn=[ get_varName(ave) for ave in ve]
    vars2elems=dict(zip(*[vn,ve]))
    return vars2elems

def init_filters():
    global filters2choices2elems
    global f2c2e
    f2c2e= filters2choices2elems={}
    
    for afe in get_filterElems():
        c2e={}
        
        for ace in get_filterChoiceElems(afe):
            c2e[get_filterChoiceName(ace)]=ace
            
        f2c2e[get_filterName(afe)]=c2e
        
    return f2c2e
    

#the titles give the variable names
def get_varElems():
    """gets the fields elements checkboxes.
    they are all: class=checkbox, name=VarName, id=VarName"""
    return tbls['fields'].find_elements_by_name("VarName")

def get_varName(varElem,nameid='title'):
    """
    title attrib shows up in the page and value attriib shows
    in the csv as CapitalWords and CAPTALS_WORDS respecively"""
    return varElem.get_attribute(nameid)

def selectVarElem(varElem):
    if varElem.is_selected() is False:
        varElem.click()
def clearVarElem(varElem):
    if varElem.is_selected() is True:
        varElem.click()
def clearVarSelections():
    for avare in vars2elems.values():
        clearVarElem(avare)

def selectVar(varName):
    selectVarElem(vars2elems[varName])



#utils
def up1(elem):
    """returns the parent elem of elem"""
    return elem.find_element_by_xpath('..')
def up(elem,by=1):
    for i in xrange(by):
        elem=up1(elem)
    return elem


def get_Description(chkboxElem):
    r = up(chkboxElem,by=2)
    d= r.find_elements_by_class_name('dataTD')[1] #the second one
    return d.text

def get_lookupTblElem(chkboxElem):
    """go up the hierarchy two levels to get to table row,
    then find look up link
    you get NoSuchElemException if no lookup link"""
    r = up(chkboxElem,by=2)#cb.find_element_by_xpath('../..')
    link = r.find_element_by_partial_link_text('Lookup')
    return link #you get NoSuchElementException if there is no lookup tbl


def get_filterElems():
    """gets the filter elements"""
    return tbls['filters'].find_elements_by_class_name('slcBox')

def get_filterName(filterElem,nameid='id'):
    """gets filter name
    id=name=GEOGRAPHY/YEAR/PERIOD"""
    return filterElem.get_attribute(nameid)

def get_filterChoiceElems(filterElem):
    """returns a list of filter choice elements"""
    return Select(filterElem).options 
def get_filterChoiceName(choiceElem):
    return choiceElem.text

def selectFilterChoice(FilterName,choiceName):
    f2c2e[FilterName][choiceName].click()

def get_downloadElem():
    return tbls['download'].find_element_by_name("Download")
def clickDownload(): get_downloadElem().click()


#todo a table is defined by its variables, make hash of vars for the
#file name just string together the var names?

#trying not to have any derived fields
default_fields=['Year','Month','DayofMonth'
                ,'UniqueCarrier'
                ,'OriginAirportID'
                ,'DestAirportID'
                ,'CRSDepTime','DepDelay'
                ,'CRSArrTime','ArrDelay'
                ,'Cancelled','CancellationCode','Diverted'
                ,'CRSElapsedTime','ActualElapsedTime',
                ]



from time import sleep   
def waitDownload(s=1):
    while isDownloadFinished() is False:
        sleep(s); pass
    
def download(yr,mo,geo='All',varsList=default_fields
             ,wait=True):
    #waits for a previous download to finish
    if wait==True:
        waitDownload()
    
    clearChkBoxes()
    
    if geo=='All': geo='All '
    yr=str(yr)

    selectFilterChoice('GEOGRAPHY',geo)
    selectFilterChoice('XYEAR',yr)
    selectFilterChoice('FREQUENCY',mo)

    for avar in varsList:
        selectVar(avar)

    clickDownload()



import scrape_config
# import hashlib
# import os
# def uniquefn(yr,mo,geo):
#     return hashlib.md5(str(yr)+str(mo)+str(geo)).hexdigest()
# def procDownload(yr,mo,geo):
#     dlfp=os.path.join(scrape_config.browser_download_dir
#         ,os.listdir(scrape_config.browser_download_dir)[0]
import os
def isDownloadFinished():
    #VERY HACKY!
    bdd=scrape_config.browser_download_dir
    for afn in os.listdir(bdd):
        if 'ONTIME' in afn:
            if 'download' in afn:
                return False
    return True


def downloadAll(niceness=0):
    geo='All'
    for ayr in f2c2e['XYEAR']:
        for amo in f2c2e['FREQUENCY']:
            download(ayr,amo,geo=geo,wait=True)
            sleep(niceness)
    return
    

#todo set download dir in config
