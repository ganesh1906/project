from tkinter import *
from mysql import *
import tkinter
from tkinter import *
import mysql.connector as mysql


root = Tk()
tkvar = StringVar(root)
def form1():
    root1=Tk()
    root1.geometry('800x800')
    label=tkinter.Label(root1,text="User tittle",font=("Helvetica", 15))
    label.place(x=50,y=50)
    clicked = StringVar(root1)
    variable = StringVar(root1)
    variable.set("Mr")
    w = OptionMenu(root1, variable, "Mrs", "Miss", "Dr")
    w.pack()
    w.place(x=185,y=50)
    def change_dropdown(*args):
         print( clicked.get() )
    clicked.trace('w', change_dropdown)
    label1=tkinter.Label(root1,text="User name",font=("Helvetica", 15))
    label1.place(x=50,y=100)
    entry=tkinter.Entry(root1)
    entry.place(x=185,y=108)
    label2=tkinter.Label(root1,text="User Age",font=("Helvetica", 15))
    label2.place(x=50,y=150)
    entry1=tkinter.Entry(root1)
    entry1.place(x=185,y=158)
    label3=tkinter.Label(root1,text="Interest in college subject",font=("Helvetica", 15))
    label3.place(x=50,y=208)
    cbutton=tkinter.Checkbutton(root1,text="Enterprise java")
    cbutton.place(x=50,y=240)
    cbutton1=tkinter.Checkbutton(root1,text="Linux")
    cbutton1.place(x=50,y=260)
    cbutton2=tkinter.Checkbutton(root1,text="IOT")
    cbutton2.place(x=50,y=280)
    cbutton3=tkinter.Checkbutton(root1,text="AWP")
    cbutton3.place(x=50,y=300)
    cbutton2=tkinter.Checkbutton(root1,text="SPM")
    cbutton2.place(x=50,y=320)
    label4=tkinter.Label(root1,text="Interested in Music",font=("Helvetica", 15))
    label4.place(x=50,y=370)
    var=StringVar()
    rbutton=tkinter.Radiobutton(root1,text="Yes",variable=var,value =1)
    rbutton.place(x=235,y=375)
    rbutton1=tkinter.Radiobutton(root1,text="No",variable=var,value =2)
    rbutton1.place(x=295,y=375)
    def submit():
        conn=mysql.connect(user='root', password='root')
        cursor=conn.cursor()
        cursor.execute("use ganesh")
        cursor.execute('CREATE TABLE IF NOT EXISTS UserInfo(name varchar(200), age int(20))')
        cursor.execute('INSERT INTO UserInfo VALUES(%s,%s)', (entry1.get(), entry2.get()))
        conn.commit()
    b3=tkinter.Button(root1,text='Submit',height=3, width=19,command="submit")
    b3.place(x=50,y=420)
    b4=tkinter.Button(root1,text='Form2',height=3, width=19,command=form2)
    b4.place(x=50,y=480)
    
    root1.mainloop()
def form2():
    root2=Tk()
    root2.geometry('800x800')
    def only_numbers(char):
        return char.isdigit()

    validation = root2.register(only_numbers)
    
    label5=tkinter.Label(root2,text="Enetr 10th marks",font=("Helvetica", 15))
    label5.place(x=50,y=100)
    entry3=tkinter.Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry3.place(x=220,y=108)
    label6=tkinter.Label(root2,text="Enetr 12th marks",font=("Helvetica", 15))
    label6.place(x=50,y=150)
    entry4=tkinter.Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry4.place(x=220,y=158)
    label7=tkinter.Label(root2,text="Enetr Graduation marks",font=("Helvetica", 15))
    label7.place(x=50,y=200)
    entry5=tkinter.Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry5.place(x=280,y=208)
    label8=tkinter.Label(root2,text="Enetr Post Graduation marks",font=("Helvetica", 15))
    label8.place(x=50,y=250)
    entry6=tkinter.Entry(root2, validate="key", validatecommand=(validation, '%S'))
    entry6.place(x=315,y=258)
    label9=tkinter.Label(root2,text="others Examination name",font=("Helvetica", 15))
    label9.place(x=50,y=300)
    entry7=tkinter.Entry(root2)
    entry7.place(x=305,y=308)
    label9=tkinter.Label(root2,text="others Examination marks",font=("Helvetica", 15))
    label9.place(x=50,y=350)
    entry8=tkinter.Entry(root2,validate="key", validatecommand=(validation, '%S'))
    entry8.place(x=305,y=358)
    def submit2():
        conn=mysql.connect(user='root', password='root')
        cursor=conn.cursor()
        cursor.execute("use ganesh")
        cursor.execute('CREATE TABLE IF NOT EXISTS UserMarks(10th int(20), 12th int(20), Graduation int(20), PG int(20), OtherExam varchar(200), OtherMarks int(20) )')
        cursor.execute('INSERT INTO UserMarks VALUES(%s,%s,%s,%s,%s,%s)', (entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get()))
        conn.commit()
    b5=tkinter.Button(root2,text='Submit',height=3, width=19,command=submit2)
    b5.place(x=50,y=420)
    b6=tkinter.Button(root2,text='Form1',height=3, width=19,command=form1)
    b6.place(x=50,y=480)
    



l=tkinter.Label(root,text="Select the Any Form Frist",font=("Helvetica", 19,"bold"))
l.place(x=600,y=100)
b1=tkinter.Button(root,text='Form 1',height=3, width=19,command=form1)
b1.place(x=600,y=200)
b2=tkinter.Button(root,text='Form 2',height=3, width=19,command=form2)
b2.place(x=755,y=200)


root.mainloop()
