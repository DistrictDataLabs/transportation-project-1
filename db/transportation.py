from sqlalchemy import create_engine
from resources import dbs
dbd='mysql'
tdb=dbs[dbd]
engine=create_engine('%s://%s:%s@%s:%s/%s' % \
                     (dbd
                      , tdb['user'], tdb['pw']
                     ,tdb['host'],tdb['port']
                     ,tdb['db'] ))
#conn=engine.connect()
from sqlalchemy.engine.reflection import Inspector
insp=Inspector(engine)#(conn)
from sqlalchemy import MetaData
md=MetaData(engine);md.reflect()

def get_table_info(tbl_nm):
    """returns a dict with keys 'attrib' for each col"""
    for ti in insp.get_columns(tbl_nm):
        yield ti

from sqlalchemy.sql import and_,select
from sqlalchemy import Table
flights=md.tables['flights']

