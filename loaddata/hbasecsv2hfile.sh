#HADOOP_CLASSPATH=`${HBASE_HOME}/bin/hbase classpath`
#${HADOOP_HOME}/bin/hadoop jar ${HBASE_HOME}/hbase-VERSION.jar importtsv -Dimporttsv.columns=HBASE_ROW_KEY,d:c1,d:c2 -Dimporttsv.bulk.output=hdfs://storefileoutput datatsv hdfs://inputfile
#direct
#$ bin/hbase org.apache.hadoop.hbase.mapreduce.ImportTsv -Dimporttsv.columns=a,b,c <tablename> <hdfs-inputdir>
#gen store files

#export HADOOP_CLASSPATH="hbase classpath"
#$HADOOP_HOME/bin/hadoop jar /usr/local/hbase/lib/hbase-common-0.96.2-hadoop2.jar importtsv \
$HBASE_HOME/bin/hbase org.apache.hadoop.hbase.mapreduce.ImportTsv \
'-Dimporttsv.separator=|'   \
-Dimporttsv.columns=HBASE_ROW_KEY,all:YEAR,all:QUARTER,all:MONTH,all:DAY_OF_MONTH,all:DAY_OF_WEEK,all:FL_DATE,all:UNIQUE_CARRIER,all:AIRLINE_ID,all:CARRIER,all:TAIL_NUM,all:FL_NUM,all:ORIGIN_AIRPORT_ID,all:ORIGIN_AIRPORT_SEQ_ID,all:ORIGIN_CITY_MARKET_ID,all:ORIGIN,all:ORIGIN_CITY_NAME,all:ORIGIN_STATE_ABR,all:ORIGIN_STATE_FIPS,all:ORIGIN_STATE_NM,all:ORIGIN_WAC,all:DEST_AIRPORT_ID,all:DEST_AIRPORT_SEQ_ID,all:DEST_CITY_MARKET_ID,all:DEST,all:DEST_CITY_NAME,all:DEST_STATE_ABR,all:DEST_STATE_FIPS,all:DEST_STATE_NM,all:DEST_WAC,all:CRS_DEP_TIME,all:DEP_TIME,all:DEP_DELAY,all:DEP_DELAY_NEW,all:DEP_DEL15,all:DEP_DELAY_GROUP,all:DEP_TIME_BLK,all:TAXI_OUT,all:WHEELS_OFF,all:WHEELS_ON,all:TAXI_IN,all:CRS_ARR_TIME,all:ARR_TIME,all:ARR_DELAY,all:ARR_DELAY_NEW,all:ARR_DEL15,all:ARR_DELAY_GROUP,all:ARR_TIME_BLK,all:CANCELLED,all:CANCELLATION_CODE,all:DIVERTED,all:CRS_ELAPSED_TIME,all:ACTUAL_ELAPSED_TIME,all:AIR_TIME,all:FLIGHTS,all:DISTANCE,all:DISTANCE_GROUP,all:CARRIER_DELAY,all:WEATHER_DELAY,all:NAS_DELAY,all:SECURITY_DELAY,all:LATE_AIRCRAFT_DELAY,all:FIRST_DEP_TIME,all:TOTAL_ADD_GTIME,all:LONGEST_ADD_GTIME,all:DIV_AIRPORT_LANDINGS,all:DIV_REACHED_DEST,all:DIV_ACTUAL_ELAPSED_TIME,all:DIV_ARR_DELAY,all:DIV_DISTANCE,all:DIV1_AIRPORT,all:DIV1_AIRPORT_ID,all:DIV1_AIRPORT_SEQ_ID,all:DIV1_WHEELS_ON,all:DIV1_TOTAL_GTIME,all:DIV1_LONGEST_GTIME,all:DIV1_WHEELS_OFF,all:DIV1_TAIL_NUM,all:DIV2_AIRPORT,all:DIV2_AIRPORT_ID,all:DIV2_AIRPORT_SEQ_ID,all:DIV2_WHEELS_ON,all:DIV2_TOTAL_GTIME,all:DIV2_LONGEST_GTIME,all:DIV2_WHEELS_OFF,all:DIV2_TAIL_NUM,all:DIV3_AIRPORT,all:DIV3_AIRPORT_ID,all:DIV3_AIRPORT_SEQ_ID,all:DIV3_WHEELS_ON,all:DIV3_TOTAL_GTIME,all:DIV3_LONGEST_GTIME,all:DIV3_WHEELS_OFF,all:DIV3_TAIL_NUM,all:DIV4_AIRPORT,all:DIV4_AIRPORT_ID,all:DIV4_AIRPORT_SEQ_ID,all:DIV4_WHEELS_ON,all:DIV4_TOTAL_GTIME \
-Dimporttsv.bulk.output=hdfs://localhost:9000/flightsH flights file:/home/transportation_data/data/scraped/bts/dontsync/load.psv \
-Dimporttsv.skip.bad.lines=true \
-Djava.library.path=$HBASE_HOME/lib 


