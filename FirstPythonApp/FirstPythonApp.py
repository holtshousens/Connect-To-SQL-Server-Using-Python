import os

class myClass:
    def myClass(aName):
        name = aName

    def myFunction(name):
        print("This is " + name + "'s function")

    def getDirectoryContents(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith((".py")):
                    print(name)

    def getDirectoryContentsPrint(path):
        pythonFiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(path)
                    for name in files 
                        if name.endswith((".py"))]
        print(pythonFiles)




#myClass.myFunction("Sean")

#myClass.getDirectoryContents("./")

#myClass.getDirectoryContentsPrint("./")
import pypyodbc 

from xml.dom import minidom
xmldoc = minidom.parse('./config.xml')
configdriver = xmldoc.getElementsByTagName('driver')
driver = configdriver[0].attributes['name'].value
configserver = xmldoc.getElementsByTagName('server')
server = configserver[0].attributes['name'].value
configdatabase = xmldoc.getElementsByTagName('database')
database = configdatabase[0].attributes['name'].value


connection = pypyodbc.connect('Driver=' + driver + 'Server=' + server + 'Database=' + database) 

cursor = connection.cursor() 

SQLCommand = ("SELECT Name FROM dbo.Merchants") 

cursor.execute(SQLCommand) 

results = cursor.fetchone() 

while results:
     print(str(results[0]))
     results = cursor.fetchone() 

connection.close()