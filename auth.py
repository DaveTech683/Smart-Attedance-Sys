from tkinter import *
from tkinter import messagebox
import mysql.connector

def Auth():
    root = Tk()
    root.title("AUMAS")
    height = root.winfo_screenheight()//2
    width = (root.winfo_screenwidth())//2
    root.geometry("{}x{}".format(width, height))
    # this  brings the window to the top
    # root.attributes('-topmost',True)
    # root.eval('tk::PlaceWindow . right')

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        pass

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

    def insert_auth():
        
        fullname = entry_name.get()
        user= entry_user.get()
        password= entry_pass.get()
        phone= entry_phone.get()
        

    
        if fullname == "" or user == "" or password =="" or phone =="":
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
                query = """INSERT INTO lecturers(
                Full_name, Password, telephone, Username
                )
                VALUES(%s,%s,%s,%s)"""
                vals = (fullname,password, phone,user)
                cursor.execute(query,vals)
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Successful","Record added successfully")
            except:
                messagebox.showerror("Error","Record already exist")

    frame_auth= Frame(root,width=width, height=height)
    frame_auth.place(x=0,y=0)

    lbl_title= Label(frame_auth, text="Authorization Page",font=('calibre',25,'normal'), bg="green", fg="white")
    lbl_title.place(x=210, y= 30)


    lbl_name= Label(frame_auth, text="Full Name")
    lbl_name.place(x=80, y= 90)

    entry_name = Entry(frame_auth, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_name.place(x =80, y = 110, height=35, width=500)

    global login_user
    login_user =[]

    lbl_user= Label(frame_auth, text="Usernanme")
    lbl_user.place(x=80, y=150)

    global entry_user
    entry_user = Entry(frame_auth, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_user.place(x =80, y = 170, height=35, width=500)

    login_user.append(entry_user.get())
    global login_user1
    login_user1 = login_user

    lbl_pass= Label(frame_auth, text="Password")
    lbl_pass.place(x=80, y=210)

    entry_pass = Entry(frame_auth, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_pass.place(x =80, y = 230, height=35, width=500)


    lbl_phone= Label(frame_auth, text="Telephone:")
    lbl_phone.place(x=80, y=270)

    entry_phone = Entry(frame_auth, font=('calibre',12,'normal'), bg="green", fg="WHITE")
    entry_phone.place(x =80, y = 290, height=35, width=500)

    btn_reg = Button(frame_auth, text="Submit", command=insert_auth)
    btn_reg.place(x=280, y=340)


    root.mainloop()