import  MySQLdb


conn = MySQLdb.connect("localhost",'root','','student')
curr = conn.cursor()

curr.execute("""CREATE TABLE EMPLOYEE(id int,name varchar(10))""")
# curr.execute("""SELECT *FROM EMP""")

conn.close()
