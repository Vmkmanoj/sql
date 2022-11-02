import sqlite3

con=sqlite3.connect(r"database.db")

cur=con.cursor()

cur.execute("""CREATE TABLE EMPLOYEENAME 
                (NAME TEXT,
                AGE INTERGER
                CLASS TEXT
                SALARY INTERGER)



""")


con.commit()
con.close()