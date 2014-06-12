#go thru dirs of varsetunique
#take a data file csv in it and take header line to make a table
#import the data to the table

# CSV Import

# Use the ".import" command to import CSV (comma separated value) data into an SQLite table. The ".import" command takes two arguments which are the name of the disk file from which CSV data is to be read and the name of the SQLite table into which the CSV data is to be inserted.

# Note that it is important to set the "mode" to "csv" before running the ".import" command. This is necessary to prevent the command-line shell from trying to interpret the input file text as some other format.

# sqlite> .mode csv
# sqlite> .import C:/work/somedata.csv tab1
# There are two cases to consider: (1) Table "tab1" does not previously exist and (2) table "tab1" does already exist.

# In the first case, when the table does not previously exist, the table is automatically created and the content of the first row of the input CSV file is used to determine the name of all the columns in the table. In other words, if the table does not previously exist, the first row of the CSV file is interpreted to be column names and the actual data starts on the second row of the CSV file.

# For the second case, when the table already exists, every row of the CSV file, including the first row, is assumed to be actual content. If the CSV file contains an initial row of column labels, that row will be read as data and inserted into the table. To avoid this, make sure that table does not previously exist.

from scrape.BTS import walk_extractedFiles
from scrape.scrape_config import extract_to

from db.db import sqlite3 as db

import os

dbf=os.path.join(extract_to,'load.'+db.myext)
db.create(dbf)
ldb=db(dbf)

#sql stmts: begin transaction and drop tbl if exists
#use csv module to make data oriented for
#http://www.sqlite.org/cvstrac/wiki?p=ImportingFiles
#maybe put the csv in a tmp file

import csv
w=walk_extractedFiles()
cdir,cfile=w.next()
cfile=cfile.next()
co=csv.reader(open(cfile),delimiter=',') #extra , at end of each line so use ,\n as line term

def loadCSVs(iCSVs):
    ic=iCSVs#iter CSVs
    ldb.exec_script
    
