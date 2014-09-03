/*#this is to fmt the data the way mysql/infinidb likes it 


run as:
sqlite3 loaddb --init thisfile > output
*/
/*.mode csv */
.separator '|'
.header off
select * from T887e3aca3c;
/* need to exit to get a EOF */
.quit
