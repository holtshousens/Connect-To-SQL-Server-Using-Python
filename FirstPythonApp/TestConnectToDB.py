
# How to use the class methods
import ConnectToDB

myDriver, myServer, myDatabase = ConnectToDB.ConnectToDB.connectionstring()
myCursor, myConnection = ConnectToDB.ConnectToDB.connect(driver=myDriver, server=myServer, database=myDatabase)
ConnectToDB.ConnectToDB.getsample(cursor=myCursor, schemaname="dbo", tablename="Merchants", fieldname="Name")
ConnectToDB.ConnectToDB.disconnect(connection=myConnection)
