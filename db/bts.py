
from resources import dirs
import os

def loadDBpth():return os.path.join(dirs['data_store'],'data/scraped/bts/load.sqlite') 

def locate_loadDB():
    """finds path of load db..returns None if not found"""
    loc= loadDBpth()
    if os.path.exists(loc)==True: return loc
    else: return None

load_dbpth=locate_loadDB()

def create_loadDB(overwrite=False):
    pass
    
