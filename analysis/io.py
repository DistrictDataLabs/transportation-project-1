"""
module to take care and process columns related to the input and output
of the analysis/modeling
"""

#i/o grp + transformation = analysis group


def get_io_grps():
    import os
    #io variables file
    iof=open(os.path.splitext(__file__)[0]+'.csv')
    grp_names=iof.readline().replace('\n','').split(',')[1:]; 
    import csv
    iof.seek(0)
    rdr=csv.DictReader(filter(lambda row: not(row[0]==',' or row[0]=='#'  )
                              , iof))
    grps=dict.fromkeys(grp_names)
    for agrp in grps: grps[agrp]=[]
    for aline in rdr:
        iov=aline['var']
        for agrp in grp_names:
            if 'x' in aline[agrp]:
                grps[agrp].append(iov) 
    return grps
    
from sqlalchemy import select
from sqlalchemy.sql import and_
from db.sql import sql_dec #col can be processed
from db.transportation import flights

def select_flights(origin,dest,analysis_columns
                   ,whereclause=[]):
    """mixNmatch strings with sqlalchemy objs in the args"""
    return select( analysis_columns \
      ,and_(flights.c.ORIGIN==origin, flights.c.DEST==dest
            ,*whereclause
            )
            )

io_grps=get_io_grps()


def _c(acol,grp):
    """want to go through io.csv instead of flights.c.acol for robustness
    #column name -> index of column list -> column name"""
    i=io_grps[grp].index(acol)
    return io_grps[grp][i]



#functions transforming columns (in sql). all return lists

from sqlalchemy.sql import case
#(UNIVAR) output analysis transformation
def fo0():
    """in flights is cancelled returns a special number (13) to go alone with delay groups"""
    return [case( [(     flights.c[_c('CANCELLED',       'o0')]==1 , 13)] #if flight is cancelled
                  ,else_=flights.c[_c('ARR_DELAY_GROUP', 'o0')]
                  )] #use it as an indicator...... in arr delay group
def fo1():
    """use cancelled as a predictor"""
    return [             flights.c[_c('CANCELLED',       'o1')]   ]
def fo2():
    """ANY delay..can delay be predicted at all?"""
    return [case( [(     flights.c[_c('ARR_DELAY_GROUP', 'o0')]>1 , 1)] 
                  ,else_=                                           0 
                  )] #
def fi0():
    """just returns the group w/o transforming anything"""
    fvars=[]
    for avar in io_grps['i0']:
        if avar in flights.c:
            fvars.append(flights.c[_c(avar,              'i0')])
    return fvars

#association b/w functions and io grps
fi={'i0':fi0}
fo={'o0':fo0,'o1':fo1,'o2':fo2}

def analysis_tbl(origin,dest,input_grp,output_grp,**kwargs):
    """makes a table with the first col as the output"""
    analysis_cols=fo[output_grp]()+fi[input_grp]()
    return select_flights(origin,dest,analysis_cols,**kwargs)

if __name__=='__main__':
    """output the sql for the table that will be analyzed
    example: python -m analysis.io LAX JFK i0 o0
    """
    import sys
    fargs=sys.argv[1:]
    from db.sql import literalquery as lq
    print str(lq(analysis_tbl(*fargs)))
