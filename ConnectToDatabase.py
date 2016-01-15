import pypyodbc connection = pypyodbc.connect('Driver={SQL Server};'
                                'Server=SEAN-PC;'
                                'Database=TransactionsDB;') cursor = connection.cursor() 
SQLCommand = ("SELECT Name "
               "FROM dbo.Merchants") cursor.execute(SQLCommand) results = cursor.fetchone() while results:
     print (str(results[0]))
     results = cursor.fetchone() connection.close()