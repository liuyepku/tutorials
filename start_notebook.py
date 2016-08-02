# infrastructure
print "Importing FeatureWorker...",
print "mif and mm..." 
import sys
sys.path.append("/home/sgiorgi/newPERMA/CoreInfrastructure/")
from FeatureWorker.featureStar import FeatureStar
from FeatureWorker.outcomeGetter import OutcomeGetter
from FeatureWorker.featureGetter import FeatureGetter
import FeatureWorker.fwConstants as fwc
from FeatureWorker.mysqlMethods import mysql_iter_funcs as mif
from FeatureWorker.mysqlMethods import mysqlMethods as mm

# pandas
print "pandas as pd...", 
import pandas as pd
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth',100)

# numpy
print "numpy as np...", 
import numpy as np

# matplotlib
print "matplotlib as mpl...",
print "pyplot as plt...",
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt

# other
print "seaborn as sns..."
import seaborn as sns

# get db                                                                                                                                                               
db = raw_input('Start sqlalchemy engine for database (or hit Enter for None): ')

if db:
    db_eng = mif.get_db_engine(db)
    print ""
    print "Engine initialized with varname 'db_eng'"
    print ""
else:
    print ""
    print "No engine initialized. Initialize with:"
    print "> db_eng = mif.get_db_engine(db)"
    print ""

# def concatDFs(dataframes):
# 	return pd.concat(dataframes, axis=0)

# def newDF(sql, index, con=db_eng):
# 	if not con:
# 		con = db_eng
# 	return pd.read_sql(sql=sql, con=con, index_col=index)

# print "Methods:"
# print "\tconcatDFs(dataframes)"
# print "\tnewDF(sql, index, con=db_eng)"