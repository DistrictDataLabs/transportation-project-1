

#1. get load sqlite tables
#2. 

from resources import files as ldp
ldp=ldp['bts_sqlt3']

import sqlite3
conn=sqlite3.connect(ldp)
cur=conn.cursor()

def get_flight_tables():
    it= cur.execute('select name from sqlite_master where type=\'table\'')
    for at in it:
        yield at[0]


def get_flight_vars(tblName='T887e3aca3c'):
    it=cur.execute('pragma table_info(\'' +tblName+ '\');')
    for ar in it:
        yield ar[1]

from loaddata.types import make_typesDict
def gen_create_flights_table(engine='InfiniDB'):
    cols=list(get_flight_vars())
    td=make_typesDict('mysql')

    #chk
    for adt in td:
        if (adt not in cols) and (adt != 'DEFAULT_DTYPE'):
            raise ValueError\
                     ('data type '+adt+ ' does not corespond to a col')

    typestr=''
    for acol in cols:
        if acol in td: ct=td[acol]
        else: ct=td['DEFAULT_DTYPE']
        typestr+=acol+' '+ct+','
        
    typestr=typestr[:-1]# take out last comma
    
    ctc='create table flights ( ' + typestr + ') '\
      +' engine='+engine  \
      + ';'
    return ctc

if __name__=='__main__':
    import sys
    try: tablenm=sys.argv[1]
    except: tablenm='flights'

    if tablenm == 'flights':
        print gen_create_flights_table()
