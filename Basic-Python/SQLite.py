#PYTHON AND SQL
print("PYTHON AND SQLITE3")
import sqlite3;

#print(dir(sqlite3));
#print(help(sqlite3));
#Note that the following code blocks would normally be inside functions, but for the sake of this demonstration are show as so:

#CONNECCT TO A DATABASE
connectdb = sqlite3.connect('test.db');

#CREATE A DATABASE
with connectdb: 
    cursor = connectdb.cursor()     #use the .cursur() method to influence the db
    cursor.execute("CREATE TABLE IF NOT EXISTS table_Name(\
        attribute_ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_fname TEXT,\
        col_lname TEXT,\
        col_email TEXT\
        )")   #use the .execute() command to pass in a SQL statement
    connectdb.commit()
connectdb.close();

#ADD TO A DATABASE
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

#QUERY A DATABASE
connectdb = sqlite3.connect('test.db');
with connectdb: 
    cursor = connectdb.cursor()     #use the .cursur() method to influence the db
    cursor.execute("SELECT col_fname, col_lname, col_email FROM table_Name\
        WHERE col_fname = 'Sarah' ")
    variableName = cursor.fetchall()
    for item in variableName:
        variableString = "First Name: {}\nLastName: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(variableString);    
connectdb.close();

#ALTER A DATABASE: ADD A COLUMN
"""
connectdb = sqlite3.connect('test.db');
with connectdb: 
    cursor = connectdb.cursor()     #use the .cursur() method to influence the db
    cursor.execute("ALTER TABLE table_Name ADD col_files TEXT")
    connectdb.commit()
"""

#UPDATE A DATABASE: ADD OBJECTS THAT MEET A CONDITION
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
