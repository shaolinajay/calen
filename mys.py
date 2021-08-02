import mysql.connector
con=mysql.connector.connect(host="locallost",user="Ajay",password="root",database="pyt")
if con:
    print('ues')
else:
    print("no")