import pyodbc 

# Read config parameters

from xml.dom import minidom
from pyodbc import ProgrammingError

def extractConnectionString():
    xmldoc = minidom.parse('./config.xml')
    configdriver = xmldoc.getElementsByTagName('driver')
    driver = configdriver[0].attributes['name'].value
    configserver = xmldoc.getElementsByTagName('server')
    server = configserver[0].attributes['name'].value
    configdatabase = xmldoc.getElementsByTagName('database')
    database = configdatabase[0].attributes['name'].value 
    return driver, server, database 

# connect to sql server
def connectToDB(driver, server, database):
    try:
        connection = pypyodbc.connect('Driver=' + driver + 'Server=' + server + 'Database=' + database) 
    except ProgrammingError as error:
        print("Programming Error: ", error)
    else:
        cursor = connection.cursor() 
        print("*** Connection to " + server + " Established ***")
        return cursor, connection

# return top 100 rows
def returnTop100(cursor, schemaname, tablename, fieldname):
    SQLCommand = ("SELECT TOP 100 " + fieldname + " FROM " + schemaname + "." + tablename) 
    print("*** Executing script: " + SQLCommand + " ***")
    cursor.execute(SQLCommand) 
    #fetch results and display to console
    print("*** Printing Result START ***")
    results = cursor.fetchone() 
    while results:
         print(str(results[0]))
         results = cursor.fetchone() 
    print("*** Printing Result END ***")

def disconnectFromDB(con):
    con.close()
    print("*** Disconnection made ***")

myDriver, myServer, myDatabase = extractConnectionString()
myCursor, myConnection = connectToDB(myDriver, myServer, myDatabase)
returnTop100(myCursor, "dbo", "Merchants", "Name")
disconnectFromDB(myConnection)