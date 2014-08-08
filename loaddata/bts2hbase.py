import happybase
import sqlite3



from resources import files as sqltfn
sqltfn=sqltfn['bts_sqlt3']
sqltblnm='T887e3aca3c' #not programmatic :(

sqlconn=sqlite3.connect(sqltfn)
sqltbl=sqlconn.execute('select * from %s' %(sqltblnm))
sqlcolnames = list(map(lambda x: x[0], sqltbl.description))

hbcolnames=['all:'+acol for acol in sqlcolnames]

#start thrift server first
hbconn=happybase.Connection('localhost')
hbtbl=hbconn.table('flights')

def importdata():
    rk=0
    with hbtbl.batch(batch_size=100000) as b:
        while True:
            try:
                rk+=1
                b.put(str(rk), dict(zip(hbcolnames,sqltbl.fetchone())) )
            except:
                break
            if rk%1000==0:print rk



if '__main__'==__name__:
    importdata()


