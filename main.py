# example 7.1
import sqlite3


#Connect to a SQLite Database....with SQL Server and pyodbc we would need login info and server name
myConnection = sqlite3.connect("MyDB")

#get a cursor so we can send commands to the server
myCursor = myConnection.cursor()

#create a table to put some data in (If it doesnt already exist)
myCursor.execute("""
CREATE TABLE IF NOT EXISTS Customer(
  ID INTEGER PRIMARY KEY AUTOINCREMENT, 
  Name STRING,
  Email STRING,
  Salary real
);
""")


#Insert Some Data
myCursor.execute("""
INSERT INTO CUSTOMER(Name, Email, Salary) 
VALUES ('Liz', 'Liz@Liz.com', 94000);
""")

myCursor.execute("""
INSERT INTO CUSTOMER(Name, Email, Salary) 
VALUES ('Sue', 'Sue@Sue.com', 88000);
""")

myCursor.execute("""
INSERT INTO CUSTOMER(Name, Email, Salary) 
VALUES ('Ed', 'Ed@Ed.com', 22000);
""")

myCursor.execute("""
INSERT INTO CUSTOMER(Name, Email, Salary) 
VALUES ('Ron', 'Ron@Ron.com', 143000);
""")

myCursor.execute("""
INSERT INTO CUSTOMER(Name, Email, Salary) 
VALUES ('Tom', 'Tom@Tom.com', 76000);
""")

myCursor.execute("""
INSERT INTO CUSTOMER(Name, Email, Salary) 
VALUES ('Jo', 'Jo@Jo.com', 299000);
""")


#Select the Data
myCursor.execute("""
SELECT * 
FROM CUSTOMER;
""")

print("\nSELECT after INSERT:")
#Walk through the data...
myRows = myCursor.fetchall() 

#loop one Row at a time and print the entire row (All Fields\Columns)
for r in myRows:
  print(r)

#Update Tom To Tommy Boy
myCursor.execute("""
UPDATE Customer 
SET Name = 'Tommy Boy' 
WHERE Name = 'Tom';
""")


#Select the Data Again
myCursor.execute("""
SELECT * 
FROM CUSTOMER;
""")

print("\nSELECT after UPDATE:")
#Walk through the data...
myRows = myCursor.fetchall() 

#loop one Row at a time and print the entire row (All Fields\Columns)
for r in myRows:
  print(r)


#Delete Ed using the ID of 3
myCursor.execute("""
DELETE FROM CUSTOMER 
WHERE ID=3;
""")

print("\nSELECT after DELETE:")
#Select the Data Again
myCursor.execute("""
SELECT * 
FROM CUSTOMER;
""")

#Walk through the data...
myRows = myCursor.fetchall() 

#loop one Row at a time and print the entire row (All Fields\Columns)
for row in myRows:
  print("ID: " + str(row[0]) + " Name: " + row[1] + " Email: " + row[2] + " Salary: " + str(row[3]))

