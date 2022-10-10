#PYTHON AND SQL
print("PYTHON AND SQLITE3")
import sqlite3;

#print(dir(sqlite3));
#print(help(sqlite3));
#Note that the following code blocks would normally be inside functions, but for the sake of this demonstration are show as so:

##CREATE A TEMPORARY DATABSE STORED IN RAM:
#connectdb = sqlite3.connect(':memory:')    #'connectdb' is a varaible/instance - you can name the connection anything you want. 

##CREATE A DATABASE
#The first step is to CONNECT TO A DATABASE:
import sqlite3;

with sqlite3.connect('test.db') as connection:
    conn = connection.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS table_Name(\
        attribute_ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_email TEXT\
        )")                                 #use the .execute() command to pass in a SQL statement
    #connectdb.commit()                     #With Example 2, you MAY commit any changes to the database to see the updates immediately. Otherwise, they're automatically saved.
conn.close();                               #Close the connection to the database via the .close() method to avoid errors or database corruption.

#Example2
import sqlite3;
connectdb = sqlite3.connect('test.db');     #Create a variable to represent/hold/instantiate the connection to the database via the sqlite3 module and the .connect('name of the DB') method. 

with connectdb:                             #with is a python keyword to simplify exception handling
    cursor = connectdb.cursor()             #Use the .cursur() method to influence the db
    cursor.execute("CREATE TABLE IF NOT EXISTS table_Name(\
        attribute_ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_email TEXT\
        )")                                 #use the .execute() command to pass in a SQL statement
    connectdb.commit()                      #MUST use the .commit() method to commit any changes to the database
connectdb.close();                          #Close the connection to the database via the .close() method to avoid errors or database corruption.

#Example3
"""
import sqlite3;
conn = sqlite3.connect('test.db');
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")   #Create a (new) table (if one doesn't already exist) and create three attributes (columns).
#c.execute("INSERT INTO People VALUES('Ronald', 'Weasley', '42')")
conn.close()
"""

##DELETE A DATABASE - this will not execute because there is no open connection
#connectdb.execute("DROP TABLE IF EXISTS People")

##ADD TO A DATABASE
"""
connectdb = sqlite3.connect('test.db');
with connectdb:
    cursor = connectdb.cursor()     
    cursor.execute("INSERT INTO table_Name\
        (col_fname, col_lname, col_email)\
        VALUES(?, ?, ?)",\
        ('Kevin', 'Bacon', 'kbman@gmail.com'))
    cursor.execute("INSERT INTO table_Name\
        (col_fname, col_lname, col_email)\
        VALUES(?, ?, ?)",\
        ('Sarah', 'Jones', 'sarahJones99@gmail.com'))
    cursor.execute("INSERT INTO table_Name\
        (col_fname, col_lname, col_email)\
        VALUES(?, ?, ?)",\
        ('Sally', 'Mae', 'govLoans@gmail.com'))
    connectdb.commit()
connectdb.close();
"""

##QUERY A DATABASE
#Return (all) attributes for a given record
connectdb = sqlite3.connect('test.db');
with connectdb: 
    cursor = connectdb.cursor()     
    cursor.execute("SELECT col_fname, col_lname, col_email FROM table_Name\
        WHERE col_fname = 'Sarah' ")
    variableName = cursor.fetchall()
    for item in variableName:
        variableString = "First Name: {}\nLastName: {}\nEmail: {}".format(item[0], item[1], item[2])
        print(variableString);    #Needs to be WITHIN the for loop or it will only print the LAST query result.
connectdb.close();

##ALTER A DATABASE: ADD A COLUMN
"""
connectdb = sqlite3.connect('test.db');
with connectdb: 
    cursor = connectdb.cursor()     #use the .cursur() method to influence the db
    cursor.execute("ALTER TABLE table_Name ADD IF EXISTS col_files TEXT")
    connectdb.commit()
connectdb.close();
"""

##ALTER A DATABASE: DROP A COLUMN
"""
connectdb = sqlite3.connect('test.db');
with connectdb: 
    cursor = connectdb.cursor()     #use the .cursur() method to influence the db
    cursor.execute("ALTER TABLE table_Name DROP col_files")
    connectdb.commit()
connectdb.close();
"""

##ALTER A DATABASE: DELETE A ROW
"""
connectdb = sqlite3.connect('test.db');
with connectdb: 
    cursor = connectdb.cursor()     #use the .cursur() method to influence the db
    cursor.execute("DELETE FROM table_Name WHERE attribute_ID BETWEEN 6 AND 70")
    connectdb.commit()
connectdb.close();
"""

##UPDATE A DATABASE: ADD OBJECTS THAT MEET A CONDITION
"""
connectdb = sqlite3.connect('test.db');

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg');

for x in fileList:
    if x.endswith("txt"):
        with connectdb: 
            cursor = connectdb.cursor()     #use the .cursur() method to influence the db
            cursor.execute("INSERT INTO table_Name (col_files) VALUES(?)", (x,))
        print(x)
        connectdb.commit()
connectdb.close();
"""

###UPDATE A DATABASE: ADD RECORDS USING WILDCARDS - PARAMETERIZED STATEMENT
"""
variableWildCards =(("firstName1", "lastName1", "email1"), ("firstName2", "firstName2", "email2"))

with sqlite3.connect('test.db') as connection:
    conn = connection.cursor()
    conn.executemany("INSERT INTO table_Name VALUES(NULL,?,?,?)", variableWildCards);       #When using AUTOINCREMENT on a table, you must use "NULL" as the incrementing number
conn.close()
"""

#Example2
peopleValues = (('Ron', 'Weasley', 42), ('Arthur', 'Dent', 31), ('Nick', 'Tesla', 27), ('Hellen', 'Keller', 22))

with sqlite3.connect('test.db') as connection:
    conn = connection.cursor()
    conn.execute("DROP TABLE IF EXISTS People")
    conn.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")
    conn.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)

    #Query1: fetchall()
    conn.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")   #Another useful SQL command is ("SELECT * FROM People")
    for register in conn.fetchall():
        print(register);
    #Query2: fetchone() and loop over the results one at a time
    conn.execute("SELECT FirstName, LastName FROM People WHERE Age < 30")
    while True:
        row = conn.fetchone()
        if row is None:             #'None' = the absense of any value for an object, a null vlaue.
            break
        print(row)
conn.close()

#Example3
rosterList = (('Jean-Baptist Zort', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
species = 'Human';

with sqlite3.connect(':memory:') as connection:     #Create a DB in RAM
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

##UPDATE A DATABASE: ADD RECORDS USING INPUTs:
"""
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
email = input("Enter your email address: ")
varWildCards = (firstName, lastName, email)
varUpdate = ("jade@gmail.com", "Jade", "A")

with sqlite3.connect('test.db') as connection:
    conn = connection.cursor()
    conn.execute("INSERT INTO table_Name VALUES(NULL,?,?,?)", varWildCards)
    #Upate Records:
    conn.execute("UPDATE table_Name SET col_email=? WHERE col_fname=? AND col_lname=?", varUpdate)
"""

#Example2
"""
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
email = input("Enter your email address: ")

with sqlite3.connect('test.db') as connection:
    conn = connection.cursor()
    variableLineOfCode = "INSERT INTO table_Name VALUES("+ 'NULL' +", '"+ firstName +"', '"+ lastName +"', '"+ email +"')"  #Remember that if you are inserting an integer, you must convert it to a string value via: str(variableName), like str(email). 
    conn.execute(variableLineOfCode)
"""

