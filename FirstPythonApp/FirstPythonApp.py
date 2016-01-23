import pypyodbc 

# Read config parameters

from xml.dom import minidom
from pypyodbc import ProgrammingError

xmldoc = minidom.parse('./config.xml')
configdriver = xmldoc.getElementsByTagName('driver')
driver = configdriver[0].attributes['name'].value
configserver = xmldoc.getElementsByTagName('server')
server = configserver[0].attributes['name'].value
configdatabase = xmldoc.getElementsByTagName('database')
database = configdatabase[0].attributes['name'].value

# connect to sql server
def connectToDB():
    try:
        connection = pypyodbc.connect('Driver=' + driver + 'Server=' + server + 'Database=' + database) 
    except ProgrammingError as error:
        print("Programming Error: ", error)
    else:
        cursor = connection.cursor() 

# return top 100 rows
def returnTop100(schemaname, tablename):
    connectToDB()
    SQLCommand = ("SELECT TOP 100 * FROM " + schemaname + "." + tablename) 
    cursor.execute(SQLCommand) 
    #fetch results and display to console
    results = cursor.fetchone() 
    while results:
         print(str(results[0]))
         results = cursor.fetchone() 
    disconnectFromDB()


# disconnect from sql server
def disconnectFromDB():
    connection.close()