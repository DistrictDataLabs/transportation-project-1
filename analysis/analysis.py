#actual analysis here
from db.transportation import flights
from analysis.io import analysis_tbl #ONLY WORKS WITH EXECFILE!...
#..OTHERWISE io MODUEL NOT FOUND!!! WTF?!?!

from db.sql import literalquery as lq
from pandas import read_sql as rsql
from db.transportation import engine

airports=['JFK','DCA'
          ,'IAD','ATL']#should really use airport id
          #no need for more data. it doesn't help


from sqlalchemy.sql import and_,or_

def XY():
    at=analysis_tbl('i0','o2',whereclause=[ #basically filters
        (flights.c.YEAR> 2005)
        & or_(*[(flights.c.ORIGIN==aa) for aa in airports]) #python is awesome
        & or_(*[(flights.c.DEST  ==aa) for aa in airports]) #
        
        ])
    tbl=rsql(str(lq(at)),engine.raw_connection())
    tbl.dropna(subset=tbl.columns,how='any',inplace=True)
    yl=['anon_1']
    xl=list(set(tbl.columns)-set(yl))
    x,y= tbl[xl],tbl[yl]
    return x,y.values.T[0]


def labele(tbl,cols='all'):
    from sklearn.preprocessing import LabelEncoder as LE
    if cols=='all':cols=tbl.columns
    le=LE()
    for ac in tbl.columns:
        tbl.loc[:,ac]=le.fit(tbl[ac]).transform(tbl[ac]) #might have to return le
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

x,y=XY()
x=labele(x)
xtrn,xtst,ytrn,ytst=xv.train_test_split(x,y,test_size=.15)
clf=rfc.fit(xtrn,ytrn)

from sklearn.metrics import classification_report,confusion_matrix

# RandomForestClassifier(bootstrap=True, compute_importances=None,
#             criterion='gini', max_depth=None, max_features='auto',
#             max_leaf_nodes=None, min_density=None, min_samples_leaf=1,
#             min_samples_split=2, n_estimators=100, n_jobs=1,
#             oob_score=False, random_state=None, verbose=0)

# In [19]: clf.score(xtst, ytst)
# Out[19]: 0.82857682857682857

# In [20]: print classification_report( ytst , clf.predict((xtst) ))
#              precision    recall  f1-score   support

#           0       0.85      0.97      0.90      4395
#           1       0.48      0.14      0.22       896



# In [24]: clf=DummyClassifier(strategy='stratified')


# In [26]: clf.fit(xtrn, (ytrn))
# Out[26]: DummyClassifier(constant=None, random_state=None, strategy='stratifi
# )

# In [27]: print classification_report( ytst , clf.predict((xtst) ))
#              precision    recall  f1-score   support

#           0       0.83      0.84      0.83      4395
#           1       0.18      0.18      0.18       896

# avg / total       0.72      0.72      0.72      5291
# avg / total       0.79      0.83      0.79      5291
