"""
locations of resources
"""

import os

#data store is one level up
dirs={
    'data_store':os.path.join(os.path.dirname( __file__ ), '..')
    ,
    'code': os.path.join(os.path.dirname( __file__ ))
    }

def __init__(abs_path=True):
    
    for arsrc in dirs:
        dirs[arsrc]=os.path.abspath(dirs[arsrc])

    
__init__()
