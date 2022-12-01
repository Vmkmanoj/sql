from tkinter import *
from tkinter import messagebox
import sqlite3




root=Tk()
root.geometry("500x400")
font=("Arial 15")
root.config(bg="blue")

con=sqlite3.connect(r"newvalue.db")
# cur=con.cursor()
# cur.execute("""CREATE TABLE MANOJKUMAR(ID INTEGER
#                                         ,NAME TEXT)  """)
# con.commit()
# con.close()

def insert():
    value=idd.get()
    value2=namee.get()
    # row=[int(idd.get)]
    cur=con.cursor()
    cur.execute("INSERT into MANOJKUMAR values('{}','{}')".format(value,value2))
    con.commit()
    if value=="" and value2=="":
        messagebox.showerror(title="error",message="item is not enter")
    else:
    
        messagebox.showinfo(title="saved",message="item is saved")
    
    
    
def delete():
    cur=con.cursor()
    cur.execute("DELETE FROM MANOJKUMAR WHERE ID='{}'".format([idd.get()]))
    messagebox.showinfo(title="deleted",message="item delete")
    





idd=StringVar()
namee=StringVar()




Label(root,text="ENTER THE ID:",bg="blue",font=font,fg="white").place(x=30,y=70)
Label(root,text="ENTER YOUR NAME:",font=font,fg="white",bg="blue").place(x=30,y=220)
enty1=Entry(root,textvariable=idd,text="ENTER ID",width=20).place(x=220,y=75)
enty2=Entry(root,textvariable=namee,width=30).place(x=250,y=225)
Button(root,text="insert",width=15,height=2,font="arial 10",command=insert).place(x=70,y=300)
Button(root,text="delete",width=15,height=2,font="arial 10",command=delete).place(x=240,y=300)
root.mainloop()

