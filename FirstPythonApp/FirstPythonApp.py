import pypyodbc 

# Read config parameters
from xml.dom import minidom
xmldoc = minidom.parse('./config.xml')
configdriver = xmldoc.getElementsByTagName('driver')
driver = configdriver[0].attributes['name'].value
configserver = xmldoc.getElementsByTagName('server')
server = configserver[0].attributes['name'].value
configdatabase = xmldoc.getElementsByTagName('database')
database = configdatabase[0].attributes['name'].value

# connect to sql server
connection = pypyodbc.connect('Driver=' + driver + 'Server=' + server + 'Database=' + database) 
cursor = connection.cursor() 

# execute a script
SQLCommand = ("SELECT Name FROM dbo.Merchants") 
cursor.execute(SQLCommand) 

#fetch results and display to console
results = cursor.fetchone() 
while results:
     print(str(results[0]))
     results = cursor.fetchone() 

connection.close()