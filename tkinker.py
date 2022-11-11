#doing same project for best partice and adding new technics...show, lables adding button for best understanding


from tkinter import*
import sqlite3

con=sqlite3.connect(r"guidatabase.db")

cur=con.cursor()

# cur.execute("""CREATE TABLE STUDENT(
        
        
#                                 NAME TEXT,
#                                 AGE INTEGER, 
#                                 CITY TEXT,
#                                 PHONENUMBER INTEGER,
#                                 GENDER TEXT,
#                                 PHONE INTEGER)  """)

                              






def entery():

    name_enter=name.get()
    age_enter=age.get()
    city_enter=city.get()
    phone_enter=phone.get()
    gender_enter=gender.get()
    total_enter=total.get()

    cur.execute("insert into STUDENT values('{}','{}','{}','{}','{}','{}')".format(name_enter,age_enter,city_enter,phone_enter,gender_enter,total_enter))

    con.commit()
    con.close()
    Label(text="sucessfully......",font="arial 20",fg="green").place(x=220,y=430)
def show():
   cur=con.cursor()
   cur.execute("SELECT NAME,AGE,CITY,PHONENUMBER,GENDER,PHONE FROM STUDENT") 
   mano=cur.fetchall()
   A=tabulate(mano,headers=["NAME","AGE","CITY","PHONE","GENDER","FEE"])
   Label(text=A).pack()



    


root=Tk()

root.geometry("600x500")








#lable's
lab1=Label(root,text="Student Entry",font=("Arial 20"),bg="red",).pack()
lab2=Label(text="name:",font="arial 15").place(x=40,y=130)
lab3=Label(text="Age:",font="arial 15").place(x=40,y=170)
lab4=Label(text="City:",font="arial 15").place(x=40,y=210)
lab5=Label(text="Phone Number:",font="arial 15").place(x=40,y=250)
lab6=Label(text="Gender:",font="arial 15").place(x=40,y=290)
lab7=Label(text="Totalfees:",font="arial 15").place(x=40,y=330)


#stroing
name=StringVar()
age=StringVar()
city=StringVar()
phone=StringVar()
gender=StringVar()
total=StringVar()


#entrer
eny1=Entry(textvariable=name,width=30,bd=2,font="arial 10").place(x=200,y=135)
eny2=Entry(textvariable=age,width=30,bd=2,font="arial 10").place(x=200,y=175)
eny3=Entry(textvariable=city,width=30,bd=2,font="arial 10").place(x=200,y=215)
eny4=Entry(textvariable=phone,width=30,bd=2,font="arial 10").place(x=200,y=255)
eny5=Entry(textvariable=gender,width=30,bd=2,font="arial 10").place(x=200,y=295)
eny6=Entry(textvariable=total,width=30,bd=2,font="arial 10").place(x=200,y=335)

#submitbtton

sub=Button(text="submit" ,font="arial 15",command=lambda:entery()).place(x=220,y=400)
sho=Button(text="show",font="arial 15",command=lambda:show()).place(x=300,y=400)


root.mainloop()
