
import os

types_file=os.path.join(os.path.split(__file__)[0],'bts_dtypes.txt')
types_file=os.path.abspath(types_file)

typedata=[]
varNames=[]
with open(types_file) as tf:
    systems=dict.fromkeys(tf.readline().split()[1:])
    for aline in tf:
        sl=aline.split()
        typedata.append(sl)
        varNames.append(sl[0])
    
si=1
for asys in systems:
    systems[asys]=si
    si+=1
del si

def get_type(avar,asystem):
    for aline in typedata:
        if avar in aline[0]:
            return aline[systems[asystem]]


def make_typesDict(asystem):
    td={}
    for avar in varNames:
        td[avar]=get_type(avar,asystem)
    return td


# types={}
# for asys in systems:
#     types[asys]=make_typesDict(asys)

# variable sqlite numpy
# YEAR  INTEGER  int
# MONTH  INTEGER  int
# DAY_OF_MONTH  INTEGER int
# UNIQUE_CARRIER  TEXT str
# ORIGIN_AIRPORT_ID  INTEGER int
# DEST_AIRPORT_ID  INTEGER int
# CRS_DEP_TIME  TEXT str
# DEP_DELAY  INTEGER int
# CRS_ARR_TIME  TEXT int
# ARR_DELAY  INTEGER int
# CANCELLED  INTEGER bool
# CANCELLATION_CODE  TEXT str
# DIVERTED  INTEGER bool
# CRS_ELAPSED_TIME  INTEGER int
# ACTUAL_ELAPSED_TIME  INTEGER int
