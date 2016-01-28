
# How to use the class methods
import ConnectToDB

mySchema = "dbo"
myTable = "Merchants"
myField = "Name"

myDriver, myServer, myDatabase = ConnectToDB.ConnectToDB.connectionstring()
myCursor, myConnection = ConnectToDB.ConnectToDB.connect(driver=myDriver, server=myServer, database=myDatabase)
ConnectToDB.ConnectToDB.getsample(cursor=myCursor, schemaname=mySchema, tablename=myTable, fieldname=myField)
ConnectToDB.ConnectToDB.disconnect(connection=myConnection)
