import mysql.connector

class Connection():

    #defining function to connect the database
    def getConn():
        my_database = mysql.connector.connect(
            host='127.0.0.1',
            user='root', password='root',
            port = '3307',
            database='pythonproject',
        )
        return my_database


    #Closing the connection
    def closeConn(con):
        con.close()
