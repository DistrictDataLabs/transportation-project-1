#actual analysis here
from db.transportation import flights
from analysis.io import analysis_tbl #ONLY WORKS WITH EXECFILE!...
#..OTHERWISE io MODUEL NOT FOUND!!! WTF?!?!

from db.sql import literalquery as lq
from pandas import read_sql as rsql
from db.transportation import engine

def XY():
    at=analysis_tbl('DCA','JFK','i0','o2',whereclause=[flights.c.YEAR>2005])
    tbl=rsql(str(lq(at)),engine.raw_connection())
    tbl.dropna(subset=tbl.columns,how='any',inplace=True)
    yl=['anon_1']
    xl=list(set(tbl.columns)-set(yl))
    return tbl[xl],tbl[yl]


def labele(tbl,cols='all'):
    from sklearn.preprocessing import LabelEncoder as LE
    if cols=='all':cols=tbl.columns
    le=LE()
    for ac in tbl.columns:
        tbl.loc[:,ac]=le.fit(tbl[ac]).transform(tbl[ac])
    return tbl

# from sklearn.pipeline import Pipeline
# clf = Pipeline([
#   ('feature_selection', LinearSVC(penalty="l1")),
#   ('classification', RandomForestClassifier())
# ])

import numpy as np

from sklearn import cross_validation as xv
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn import svm
from sklearn import preprocessing as pp
rfc=RFC(n_estimators=50)
