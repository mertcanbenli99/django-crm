import mysql.connector

config = {
    'user': 'root',
    'password': 'password123',
    'host': 'localhost',
    'raise_on_warnings': True
}


cnx = mysql.connector.connect(**config)
# prepare a cursor object

cursorObject = cnx.cursor()

cursorObject.execute("CREATE DATABASE crmdb")

print("All done")
