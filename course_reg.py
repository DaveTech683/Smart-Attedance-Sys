from tkinter import *
from py_acr122u import nfc
import time
from tkinter import messagebox
import mysql.connector


######################This is the databasee section ################################################
########################################################################################


mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    port= 3306,
    database="aumas"
    )
cursor = mydb.cursor() 

def insert_course():
    
    fullname = entry_lecturer.get()
    course= entry_course.get()
    course_code= entry_course_code.get()
    dep = entry_dep.get()

  
    if course == "" or dep =="" or course_code =="":
        messagebox.showerror("Error","Please Fill The Boxes")  
    else:
        try:
            mydb = mysql.connector.connect(
                host = "localhost",
                user= "root",
                password = "",
                port= 3306,
                database="aumas"
                )
            cursor = mydb.cursor() 

            query_select = """SELECT Username FROM Lecturers WHERE Full_name=%s"""
            values =(fullname,)
            cursor.execute(query_select,values)
            resulted = cursor.fetchall()
            for naming in resulted:
                for names in naming:
                    pass
            mydb.commit()
           

            query_table = """CREATE TABLE IF NOT EXISTS {values}(
                Full_Name varchar(30),
                Course_code varchar(8) PRIMARY KEY,
                Department varchar (30), 
                Course_title varchar(50),
                Mdate DATE
            )""".format(values=names)
            cursor.execute(query_table)
            mydb.commit()
           

            query = """INSERT INTO {name}(
            Course_code,Full_Name,Department, Course_title 
            )
            VALUES(%s,%s,%s,%s)""".format(name=names)
            vals = (course_code,fullname,dep, course)
            cursor.execute(query,vals)
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Successful","Record added successfully")
        except Exception as e:
            messagebox.showerror("Error",e)

def crs_reg():
    root = Tk()
    root.title("AUMAS")
    height = root.winfo_screenheight()//2
    width = (root.winfo_screenwidth())//2
    root.geometry("{}x{}".format(width, height))
    # root.attributes('-topmost',True)
    # root.eval('tk::PlaceWindow . center')
    
    

    messagebox.showinfo("INFO", "Lecturer has to be an authorized user")

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        pass

    frame_course= Frame(root,width=width, height=height)
    frame_course.place(x=0,y=0)
    

    lbl_title= Label(frame_course, text="Register Course",font=('calibre',25,'normal'), bg="green", fg="white")
    lbl_title.place(x=230, y= 30)


    lbl_lecturer= Label(frame_course, text="Lecturer Name")
    lbl_lecturer.place(x=80, y= 90)
    
    global entry_lecturer
    entry_lecturer = Entry(frame_course, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_lecturer.place(x =80, y = 110, height=35, width=500)

    lbl_course= Label(frame_course, text="Course Title")
    lbl_course.place(x=80, y=150)

    global entry_course
    entry_course = Entry(frame_course, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_course.place(x =80, y = 170, height=35, width=500)

    lbl_course_code= Label(frame_course, text="Course Code")
    lbl_course_code.place(x=80, y=210)

    global entry_course_code
    entry_course_code = Entry(frame_course, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_course_code.place(x =80, y = 230, height=35, width=500)

    lbl_dep= Label(frame_course, text="Department")
    lbl_dep.place(x=80, y=270)

    global entry_dep
    entry_dep = Entry(frame_course, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_dep.place(x =80, y = 290, height=35, width=500)

    

    btn_reg = Button(frame_course, text="Register Lecturer", command=insert_course)
    btn_reg.place(x=280, y=340)



    root.mainloop()
