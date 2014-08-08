/*#this is to fmt the data the way hbase likes it 
#we have s special sqlite rowid and no header line

run as:
sqlite3 loaddb --init thisfile > output
*/
.mode csv
.header off
select ROWID,* from T887e3aca3c;
