#!/usr/bin/python
import psycopg2
import sys
import pprint
from datetime import date, timedelta

#Connect to RedShift
conn_string = "dbname='database' port='port' user='user' password='' host='HOSTNAME'";
print "Connecting to database\n        ->%s" % (conn_string)
conn = psycopg2.connect(conn_string);

cursor = conn.cursor();

#Captures Column Names 
column_names = [];
cursor.execute("Select * from table_name;");
#column_names = [desc[0] for desc in cursor.description]
#all_cols=', '.join([str(x) for x in column_names])
#print all_cols;
for record in cursor:
	print record
conn.commit();
conn.close();