import pyodbc

# Read config parameters
from xml.dom import minidom
from pyodbc import ProgrammingError


class ConnectToDB:
    def __init__(self, servertype):
        self.st = servertype

    @staticmethod
    def connectionstring():
        xmldoc = minidom.parse("./config.xml")
        configdriver = xmldoc.getElementsByTagName("driver")
        driver = configdriver[0].attributes["name"].value
        configserver = xmldoc.getElementsByTagName("server")
        server = configserver[0].attributes["name"].value
        configdatabase = xmldoc.getElementsByTagName("database")
        database = configdatabase[0].attributes["name"].value
        return driver, server, database

    # connect to sql server
    @staticmethod
    def connect(driver, server, database):
        try:
            connection = pyodbc.connect("Driver=" + driver + "Server=" + server + "Database=" + database)
        except ProgrammingError as error1:
            print("Programming error occurred: ", error1)
        except pyodbc.Error as error2:
            print("Unable to connect to server: ", error2)
        else:
            cursor = connection.cursor()
            print("*** Connection to " + server + " Established ***")
            return cursor, connection

    # return top 100 rows
    @staticmethod
    def getsample(cursor, schemaname, tablename, fieldname):
        script = ("SELECT TOP 100 " + fieldname + " FROM " + schemaname + "." + tablename)
        print("*** Executing script: " + script + " ***")
        cursor.execute(script)
        # fetch results and display to console
        print("*** Printing Result START ***")
        results = cursor.fetchone()
        while results:
            print(str(results[0]))
            results = cursor.fetchone()
        print("*** Printing Result END ***")

    @staticmethod
    def disconnect(connection):
        connection.close()
        print("*** Disconnection made ***")
