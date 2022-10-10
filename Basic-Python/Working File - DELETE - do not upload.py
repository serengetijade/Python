import sqlite3
"""
rosterList = (('Jean-Baptist Zort', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
species = 'Human';

with sqlite3.connect(':memory:') as connection:
    conn = connection.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS table_Roster(\
        Full_Name TEXT PRIMARY KEY NOT NULL, \
        Species TEXT, \
        IQ INT)")
    conn.executemany("INSERT INTO table_Roster VALUES(?,?,?)",rosterList)
    #Update the DB
    conn.execute("UPDATE table_Roster SET Species ='Human' WHERE Full_Name='Korben Dallas'")
    #Query the DB
    conn.execute("SELECT Full_Name, IQ FROM table_Roster WHERE Species ='{}'".format(species))
    rosterQuery = conn.fetchall()
    for item in rosterQuery:
        queryString = "Name: {}, IQ: {}".format(item[0], str(item[1]))
        print(queryString)      #Needs to be WITHIN the for loop or it will only print the LAST query result.
conn.close()
"""
import datetime;
import time;

Local = datetime.datetime.now()
print("The current time is: " + Local.strftime("%I")+":"+Local.strftime("%M")+" "+Local.strftime("%p")+", "+time.tzname[0])

London = time.gmtime();
print("The time in London is: " + str(London.tm_hour) + ":" + str(London.tm_min))
if 9 < London.tm_hour < 17:
    print("The London office is open")
else:
    print("The London office is closed")

#New York is 5 hours BEHIND London
print("The time in NYC is: " + str((London.tm_hour)-5) + ":" + str(London.tm_min))
if 9 < ((London.tm_hour)-5) < 17:
    print("The NYC office is open")
else:
    print("The NYC office is closed")
