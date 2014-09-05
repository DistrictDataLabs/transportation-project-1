"""
module to take care and process columns related to the input and output
of the analysis/modeling
"""

#i/o grp + transformation = analysis group



def io_grps():
    import os
    #io variables file
    iof=open(os.path.splitext(__file__)[0]+'.csv')
    grp_names=iof.readline().replace('\n','').split(',')[1:]; 
    import csv
    iof.seek(0)
    rdr=csv.DictReader(filter(lambda row: not(row[0]==',' or row[0]=='#'  )
                              , iof))
    grps=dict.fromkeys(grp_names,set())
    for aline in rdr:
        print aline
        iov=aline['var']
        for agrp in grp_names:
            if 'x' in aline[agrp]:
                grps[agrp].add(iov)
    return grps
    


from db.sql import sql_dec
def select_flights(origin,dest,analysis_columns
                   ,whereclause=[]):
    """mixNmatch strings with sqlalchemy objs in the args"""
    return flights.select(analysis_columns\
      ,and_(flights.c.ORIGIN==origin,flights.c.DEST==dest
            ,*whereclause))

