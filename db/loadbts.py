
from resources import dirs
import os


import db

def gen_DBpth(dbobj):
    if type(dbobj) is db.sqlite3:
        return os.path.join(dirs['data_store']
                        ,'data/scraped/bts/load.'+dbtype) 

def locate_DB():
    """finds path of load db..returns None if not found"""
    loc= gen_DBpth()
    if os.path.exists(loc) is True: return loc
    else: return None



# from contextlib import contextmanager as cm
# @cm
# def db(default='sqlite'):


from db import cursor as cur
        
def create_DB(overwrite=False):
    
    if (DBpth is not None) and (overwrite is True):
        os.remove(DBpth)
    c=cur(DBpth,dbtype)
    c.connect(DBpth)
    c.close()
