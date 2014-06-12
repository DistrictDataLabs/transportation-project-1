"""
process to go through csv files downloaded from bts airtravel web
"""

from scrape.BTS import walk_extractedFiles
from scrape.scrape_config import extract_to

from db.db import sqlite3 as db

import os

dbf=os.path.join(extract_to,'load.'+db.myext)
db.create(dbf)
ldb=db(dbf)

import csv

import pandas as pd


from loaddata.types import make_typesDict as mtd
#td=mtd('numpy') useless here i think

import numpy as np
def loadCSVs(**kwargs):
    walker=walk_extractedFiles()
    kwargs.setdefault('if_exists','append')
    import db
    if type(ldb) is db.db.sqlite3: kwargs['flavor']='sqlite'
    else: raise NotImplementedError
    for atbl,csvfiles in walker:
        for acsvfn in csvfiles:
            csvr=pd.read_csv(acsvfn
                             ,delimiter=',',dtype='S10')
            #extra comma at end of each file making a new column
            csvr.drop(csvr.columns[-1],axis=1,inplace=True)#
            csvr.to_sql(atbl,ldb.get_cursor().connection
                        ,**kwargs)
            #
                
    
