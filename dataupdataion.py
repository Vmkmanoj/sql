import sqlite3




con=sqlite3.connect(r"dataupdates.db")
cur=con.cursor()
# con.execute("""CREATE TABLE STUDENTNAMESS (SNO PRIMARY KEY, NAME TEXT ,AGE INTERGER,CITY TEXT)""")
# con.commit()
# con.close()

def insert(name,age,city):
    cur=con.cursor()
    cur.execute("insert into STUDENTNAMES values('{}','{}','{}')".format(name,age,city))
    con.commit()
    print("table enter succsfully")


# def delete(id):
#     cur=con.cursor()
#     cur.execute("delete from STUDENTNAMES id='{}'".format(id))
#     con.commit()

# def  update(name,age,city,id):

#     cur=con.cursor()
#     qur="update STUDENTNAMES set name={},age={},city={} where id={}".format(name,age,city,id)
#     cur.execute(qur)
#     con.commit()

def show():

    cur=con.cursor()
    cur.execute("SELECT NAME,AGE,CITY from STUDENTNAMES")
    result=cur.fetchmany()
    print(result)

while True:
    print("1.inset")
    print("2.delete")
    print("3.show")
    print("4.update")
    a=int(input(("enter the value")))
    if a==1:
        name=input("enter the name")
        age=int(input("enter the age"))
        city=input("enter the city")
        insert(name,age,city)
    # elif a==2:
    #     id=int(input("enter the id to delete"))
    #     delete(id)
    elif a==3:
        show()
    # elif a==4:
    #     id=input("enter the id name")
    #     name=input("enter the name")
    #     age=input("enter the age")
    #     city=input("enter the city")
    #     update(name,age,city,id) 
    else:
        print("ente the right number in the row")       
    