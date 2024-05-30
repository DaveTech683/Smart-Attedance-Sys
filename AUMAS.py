from tkinter import *
from py_acr122u import nfc
import time
from tkinter import messagebox
from course_reg import *
from auth import *
import mysql.connector
import tkinter.font as tkFont
from tkinter import ttk
from message import pop_up, pop_up_success


root = Tk()
root.title("AUMAS")
height = root.winfo_screenheight() 
width = (root.winfo_screenwidth())//2
root.geometry("{}x{}".format(width, height))
root.resizable(0,0)
bg = PhotoImage(file="Education-Icon-Background-PNG-Image.png")


# try:
#     # windows only (remove the minimize/maximize button)
#     root.attributes('-toolwindow', True)
# except TclError:
#     pass


def read_card():
    try:
        reader = nfc.Reader()
        try:
            time.sleep(3)
            reader.connect()
            card_info=reader.get_uid()
        except:  
            messagebox.showerror("Error","Card Not Placed on Reader")
            pass     
    except:
        messagebox.showerror("Error","Connect The NFC Reader,\n Page Will be Closed")
    try:    
        entry_code.config(text=card_info)
    except Exception as e:
        frame_student.destroy()
        reg()
        pass




mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "",
    port= 3306,
    database="aumas"
    )
cursor = mydb.cursor() 

def open_page():
    global frame_page
    frame_page = Frame(root, width=width, height=height, bg=("green"))
    frame_page.place(x=0, y=0)

    label_imh=Label(frame_page, image=bg)
    label_imh.pack()

    label_title= Label(frame_page, text="AUMAS", bg="white", fg="black", font=('helvetical', 40,"bold"))
    label_title.place(x=230, y =150)

    label_title1= Label(frame_page, text="", bg="white", fg="black", font=('helvetical', 28,"bold"))
    label_title1.place(x=40, y =250)

    label_title2= Label(frame_page, text="", bg="white", fg="black", font=('helvetical', 25,"bold"))
    label_title2.place(x=160, y =350)
    frame_page.after(2000,lambda:view_1())
    

    def view_1():
         label_title1.config(text="An Automated Attendance System")
         frame_page.after(2000,lambda:view_2())
    def view_2():
         label_title2.config(text="Log In To Get Started")
         

    frame_page.after(8000, lambda:login())
    
    
    

def login():
    frame_page.destroy()
    def query_login():
            global logs
            logs = []
            user = user_entry.get()
            password= pass_entry.get()
            logs.append(user_entry.get())

            mydb = mysql.connector.connect(
                host = "localhost",
                user= "root",
                password = "",
                port= 3306,
                database="aumas"
                )
            cursor = mydb.cursor()

            user_list=[]
            Control_query_user = """SELECT Username FROM lecturers """
            cursor.execute(Control_query_user)
            result = cursor.fetchall()
            for names in result:
                    for i in names:
                        user_list.append(i)
                        pass
            pass_list=[]
            Control_query_pass = """SELECT Password FROM lecturers """
            cursor.execute(Control_query_pass)
            results = cursor.fetchall()
            for names in results:
                    for j in names:
                            pass_list.append(j)
                            pass
                  
            if user in user_list and password in pass_list: 
                 main()
            elif user == "" or password == "":
                 messagebox.showerror("Error", "Fill In Your Details")
            else:
                 messagebox.showerror("Error", "You Are Not Authorized")
                    
    global frame_log          
    frame_log = Frame(root, width=width, height=height, bg=("green"))
    frame_log.place(x=0, y=0)

    label_title= Label(frame_log, text="LOGIN PAGE", bg="green", fg="white", font=('helvetical', 20,"bold"))
    label_title.place(x=80, y =50)

    label_user= Label(frame_log, text="Username", bg="green", fg="white", font=(12))
    label_user.place(x=80, y =145)

    global user_entry
    user_entry=Entry(frame_log, font=(8))
    user_entry.place(x=80, y=170,width=500, height=50)

 

    label_pass= Label(frame_log, text="Password", bg="green", fg="white",font=(12))
    label_pass.place(x=80, y =265)

    pass_entry=Entry(frame_log, font=(8), show="*")
    pass_entry.place(x=80, y=290,width=500, height=50)

    btn_cal = Button(frame_log, text="LOGIN", bg="white", fg="green", command=lambda:query_login())
    btn_cal.place(x = 480, y = 380, height=50, width=100)


def insert_student():

    mydb = mysql.connector.connect(
        host = "localhost",
        user= "root",
        password = "",
        port= 3306,
        database="aumas"
        )
    cursor = mydb.cursor() 
    
    fullname = entry_name.get().upper()
    matric= entry_matric.get()
    dep= entry_dep.get().upper()
    phone= entry_phone.get()
    code= entry_code.cget("text")
    level = var.get().upper()

    
    if fullname == "" or matric == "" or dep =="" or phone =="" or code =="" or level =="":
        messagebox.showerror("Error","Please Fill The Boxes") 
    else:
       
        query_code = """ SELECT Card_Code FROM students WHERE Card_Code=%s"""
        val=(code,) 
        cursor.execute(query_code,val)
        result_code = cursor.fetchall()
        if result_code ==[]:
            query = """INSERT INTO students(
            Full_name, Matric_Num, Department, Level,Telephone, Card_code
                )
            VALUES(%s,%s,%s,%s,%s,%s)"""
            vals = (fullname,matric, dep, level, phone, code)
            cursor.execute(query,vals)
            mydb.commit()
            mydb.close()
            messagebox.showinfo("Successful","Record added successfully")
        else:
            for result in result_code:
                for i in result:
                    if code == i: 
                        messagebox.showerror("Error","Code Already Registered")
                        break
                    else:
                        messagebox.showerror("Error", "Something went wrong")
        mydb.commit()
        mydb.close()




########### This is the first page which guides between the attendance and registration######################
######################## This is the first frame, frame_ home################################################
############################################################################################################
#############################################################################################################
def main():
    global frame_home
    frame_home = Frame(root,width=width, height=height, bg="green")
    frame_home.grid(ipadx=0, ipady=0)

    lbl_txt = Label(frame_home, text="AUMAS", font=('calibre',50,'normal'), bg="green")
    lbl_txt.place(x = 225, y = 80)

    lbl_txt2 = Label(frame_home, text="JUST A SMARTER WAY TO LIVE!!!", font=('calibre',20,'normal'), bg="green")
    lbl_txt2.place(x = 120, y = 200)

    btn_lecture = Button(frame_home, text="ATTENDANCE", command=lambda: attendance())
    btn_lecture.place(x = 100, y = 450, height=50, width=180)

    btn_lecture = Button(frame_home, text="REGISTRATION", command=lambda: reg())
    btn_lecture.place(x = 400, y = 450, height=50, width=180)


# ##############This frame is the second frame which is for registration page################################
#################################### Functin for student registration page###################################
#############################################################################################################
def back_reg():
     main()
     frame_reg.destroy()
     
def reg():
    frame_home.destroy()

    global frame_reg
    frame_reg = Frame(root,width=width, height=height, bg="green")
    frame_reg.grid(ipadx=0, ipady=0)

    lbl_reg = Label(frame_reg,text="Registration Page",font=('calibre',30,'normal'), bg="green", fg="white")
    lbl_reg.place(x = 190, y = 80)

    btn_exit = Button(frame_reg, text="Go Back", width=6,  command=lambda:back_reg())
    btn_exit.place(x = 630, y = 5)

    btn_student = Button(frame_reg, text="Register Students", command=student_reg)
    btn_student.place(x = 100, y = 450, height=50, width=180)

    btn_course = Button(frame_reg, text="Register Courses", command= crs_reg)
    btn_course.place(x = 400, y = 450, height=50, width=180)

    btn_auth = Button(frame_reg, text="Authorize User", command=Auth)
    btn_auth.place(x = 100, y = 550, height=50, width=180)

    btn_search = Button(frame_reg, text="Search Records", command=Query)
    btn_search.place(x = 400, y = 550, height=50, width=180)



#################################### Functin for student registration page###################################
#############################################################################################################
def back_student():
     reg()
     frame_student.destroy()

def student_reg(): 
    frame_reg.destroy()
    global frame_student
    frame_student = Frame(root,width=width, height=height, bg="green")
    frame_student.grid(ipadx=0, ipady=0)

    label_title = Label(frame_student, text="STUDENT REGISTRATION PAGE",font=('calibre',20,'normal'), bg="green")
    label_title.place(x = 80, y= 30)

    btn_exit = Button(frame_student, text="Go Back", width=6,  command=lambda:back_student())
    btn_exit.place(x = 630, y = 5)

    label_name = Label(frame_student,text="Full Name: ", font=(12),bg="green")
    label_name.place(x =80, y = 100)

    # creating a entry for input
    # name using widget Entry
    global entry_name 
    entry_name = Entry(frame_student, font=('calibre',12,'normal'))
    entry_name.place(x =80, y = 130, height=40, width=500)

    label_Matric_Num = Label(frame_student,text="Matric Number:", font=(12), bg="green")
    label_Matric_Num.place(x =80, y = 175)

    global entry_matric 
    entry_matric= Entry(frame_student, font=('calibre',12,'normal'))
    entry_matric.place(x =80, y = 200, height=40, width=500)

    label_dep = Label(frame_student,text="Department: ", font=(12), bg="green")
    label_dep.place(x =80, y = 245)

    global entry_dep
    entry_dep = Entry(frame_student, font=('calibre',12,'normal'))
    entry_dep.place(x =80, y = 270, height=40, width=500)

    label_phone = Label(frame_student,text="Telephone: ", font=(12), bg="green")
    label_phone.place(x =80, y = 315)

    global entry_phone
    entry_phone = Entry(frame_student, font=('calibre',12,'normal'))
    entry_phone.place(x =80, y = 340, height=40, width=250)

    label_level = Label(frame_student,text="Level: ", font=(12), bg="green")
    label_level.place(x =350, y = 315)

    global radio_level
    global var
    var = StringVar()
    radio_level = Radiobutton(frame_student, text="ND 1", variable=var, value="ND 1", cursor="dot")
    radio_level.select()
    radio_level.place(x =350, y = 340, height=40, width=80)

    global radio_level2
    radio_level2 = Radiobutton(frame_student, text="HND 1", variable=var, value="HND 1", cursor="dot")
    radio_level2.deselect()
    radio_level2.place(x =450, y = 340, height=40, width=80)


    label_code = Label(frame_student,text="Card Code: ", font=(12), bg="green")
    label_code.place(x =80, y = 385)

    global entry_code
    entry_code = Label(frame_student, font=('calibre',12,'normal'), bg="white", state="normal")
    entry_code.place(x =80, y = 410, height=32, width=300)

    btn_code= Button(frame_student,text="Read Card", font=(12), bg="green",fg="white", command=read_card)
    btn_code.place(x =430, y = 410, width=150)

    btn_reg= Button(root,text="Register Students", font=(12), bg="red", command=insert_student)
    btn_reg.place(x =260, y = 480, height=50, width=180)




################## This section is the attendance section ############################################
######################################################################################################
def back_att():
     main()
     frame_att.destroy()

def attendance():
    frame_home.destroy()
    global frame_att
    frame_att = Frame(root,width=width, height=height, bg="green")
    frame_att.grid(ipadx=0, ipady=0)

    label_title = Label(frame_att, text="ATTENDANCE PAGE",font=('calibre',30,'normal'), bg="green", fg='white')
    label_title.place(x = 120, y= 30)

    btn_exit = Button(frame_att, text="Go Back", width=6,  command=lambda:back_att())
    btn_exit.place(x = 630, y = 5)

    label_course = Label(frame_att,text="Course: ", font=(12),bg="green")
    label_course.place(x =80, y = 150)

    mydb = mysql.connector.connect(
        host = "localhost",
        user= "root",
        password = "",
        port= 3306,
        database="aumas"
        )
    cursor = mydb.cursor() 


    
    for log in logs:
        pass

    query = """ SELECT Course_title from {table_name} """.format(table_name = log)
    cursor.execute(query)
    result = cursor.fetchall()
    c_option = []
    for column in result:
        for i in column:
            c_option.append(i)
           

    mydb.commit()
    mydb.close()    


    helv18 = tkFont.Font(family="Helvetica", size=12)
  

    global course_drop
    clicked = StringVar()
    options = c_option
    course_drop = ttk.Combobox(frame_att, values =options, textvariable = clicked)
    course_drop.place(x =80, y = 180, width=500, height=50)
    course_drop.config(font=helv18)
    
    

    label_Dep = Label(frame_att,text="Department:", font=(12), bg="green")
    label_Dep.place(x =80, y = 290)


    global dep_drop
    clicked = StringVar()
    options = ["Computer Science"]
    dep_drop = ttk.Combobox (frame_att, values =options, textvariable = clicked)
    dep_drop.place(x =80, y = 320, width=500, height=50)
    dep_drop.config(font=helv18)
    
    label_code = Label(frame_att,text="Card Code: ", font=(12), bg="green")
    label_code.place(x =180, y = 430)

    global entry_sub_code
    entry_sub_code = Label(frame_att, font=('calibre',12,'normal'), bg="white", state="normal")
    entry_sub_code.place(x =180, y = 460, height=32, width=300)


    btn_reg= Button(frame_att,text="Take Attendance", font=(12), bg="red", command=lambda:active())
    btn_reg.place(x =260, y = 530, height=50, width=180)



# ######################## This is te active aspect of the code#############################################
############################################################################################################

def active():

    
    mydb = mysql.connector.connect(
        host = "localhost",
        user= "root",
        password = "",
        port= 3306,
        database="aumas"
        )
    cursor = mydb.cursor() 


    course = course_drop.get().upper()
    department = dep_drop.get().upper()
  
    import time
    running = True
    if course =="" or department =="":
        messagebox.showwarning("Warning","The boxes are empty")
    else:                             
        while running == True:
            try:
                reader = nfc.Reader()
                try:
                    reader.connect()
                    card_info=reader.get_uid()
                    entry_sub_code.config(text=card_info)
                    time.sleep(2)
                    code= entry_sub_code.cget("text")
                    Control_query = """SELECT Card_Code FROM students WHERE Card_Code= %s"""
                    val=(code,)
                    cursor.execute(Control_query,val)
                    result = cursor.fetchall()
                    if result == []:
                        messagebox.showwarning("Warning", "This card is not registered")
                    else:
                        for i in result:
                            for j in i:
                                if code == j:
                                        mydb = mysql.connector.connect(
                                        host = "localhost",
                                        user= "root",
                                        password = "",
                                        port= 3306,
                                        database="aumas"
                                        )
                                        cursor = mydb.cursor()
                                        Control_query_name = """SELECT  Full_Name FROM students WHERE Card_Code= %s"""
                                        val1=(code,)
                                        cursor.execute(Control_query_name,val1)
                                        resulted = cursor.fetchall()
                                        for naming in resulted:
                                            for names in naming:
                                                pass

                                        
                                        Control_query_matric = """SELECT Matric_Num FROM students WHERE Card_Code= %s"""
                                        val2=(code,)

                                        cursor.execute(Control_query_matric,val2)
                                        resulted2 = cursor.fetchall()
                                        for namings in resulted2:
                                            for imatric in namings:
                                                pass
                                        
                                        Control_query_level = """SELECT Level FROM students WHERE Card_Code= %s"""
                                        val3=(code,)
                                        cursor.execute(Control_query_level,val3)
                                        resulted3 = cursor.fetchall()
                                        for namings in resulted3:
                                            for ilevel in namings:
                                                pass

                                        name = names
                                        Matric = imatric
                                        Level = ilevel
                                    
                                        query = """INSERT INTO attendance(
                                        Matric_num,Name,Ccode,Course, Department, Level 
                                            )
                                        VALUES(%s,%s,%s,%s,%s,%s)"""
                                        vals = (Matric,name,code,course, department,Level)
                                        cursor.execute(query,vals)
                                        mydb.commit()
                                        messagebox.showinfo("SUCCESS",Matric)
                                        time.sleep(2)
                                        
                                else:
                                        pass
                                
                except Exception as e:
                    pass
                    
            except Exception as e:
                messagebox.showerror("Error",e)
                break
        mydb.commit()
        mydb.close()
   

#######################   This is the Query/Search Page ##################################################
#######################  And it is very very important ###################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


def Query():
    root = Tk()
    root.title("AUMAS")
    height = root.winfo_screenheight()
    width = (root.winfo_screenwidth())
    root.geometry("{}x{}".format(width, height))
    frame_nav_width =width//4
    frame_view_width = (width)-(width//4)
    frame_view_height = (height)-(height//8)
    frame_search_width = (width)-(width//4)
    frame_search_height = (height)-(height//8)

    frame_nav= Frame(root,width=frame_nav_width, height=height, bg="green")
    frame_nav.place(x=0,y=0)

    btn_view = Button(frame_nav, text="View Records", font=(12), bg="green", fg="white", command=lambda: view())
    btn_view.place(x = 70, y = 90, height=50, width=180)

    btn_cal = Button(frame_nav, text="Edit Records", font=(12), bg="green", fg="white", command = lambda:edit() )
    btn_cal.place(x = 70, y = 290, height=50, width=180)

    btn_cal = Button(frame_nav, text="Summary", font=(12), bg="green", fg="white", command = lambda:cal() )
    btn_cal.place(x = 70, y = 190, height=50, width=180)

    btn_cal = Button(frame_nav, text="Settings", font=(12), bg="green", fg="white", command=lambda:settings())
    btn_cal.place(x = 70, y = 390, height=50, width=180)


    frame_main= Frame(root,width=frame_search_width, height=height, bg="white")
    frame_main.place(x=340,y=0)

    label_title = Label(frame_main, text="Welcome to Aumas Query Page \n Kindly click on any of the Buttons \nin the side menu to get started", font=(15), bg="white", fg="green")
    label_title.place(x = 350, y= 200)


    def query_view():
        mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="aumas"
            )
        cursor = mydb.cursor()

        icourse = view_drop_course.get().upper()
        global idate
        idate =view_drop_date.get()
        idep = view_drop_dep.get().upper()


        # Control_query_name = """SELECT DISTINCT Name FROM attendance WHERE Course= %s 
        # AND Department=%s AND Mdate=%s AND level =%s"""
        # valname=(icourse, idep, idate, ilevel)
        # cursor.execute(Control_query_name,valname)
        # resultes = cursor.fetchall()
        # global j, names
        # global iname, inames
        # iname = []
        # if resultes == []:
        #     pop_up()
        # else:
        #     for j in resultes:
        #         for names in j:
        #             iname.append(names)
        #     mydb.commit()

        for item in label_result.get_children():
            label_result.delete(item)

        Control_query_avail = """SELECT DISTINCT Matric_num FROM attendance WHERE Course= %s 
        AND Department=%s AND Mdate=%s"""
        val1=(icourse, idep, idate)
        cursor.execute(Control_query_avail,val1)
        results = cursor.fetchall()
        avail_matric = []
        for j in results:
            for a in j:
                avail_matric.append(a)
            mydb.commit()
        Control_query_matric = """SELECT DISTINCT Full_Name, Matric_Num FROM students"""
        cursor.execute(Control_query_matric)
        resulted = cursor.fetchall()
        global i, matrics
        global imatrics, imatric
        pre_att = []
        count = 0
        if avail_matric == []:
            pop_up()
        else:
            for i in resulted:
                my_id = i[1]
                for avail in avail_matric:
                    if avail == i[1]:
                        try:
                            if count % 2==0:
                                label_result.insert("",'end', values=(i[0], i[1],"Present"), iid = my_id, tag=('odd',))
                                pre_att.append(avail)
                            else:
                                label_result.insert("",'end', values=(i[0], i[1],"Present"), iid = my_id, tag=('even',))
                                pre_att.append(avail)
                            count+=1
                        except:
                            pass
                    else:
                        pass
            
            for j in pre_att:
                for i in resulted:
                    my_id = i[1]
                    
                    if i[1] != j:
                        try:
                            if count % 2 ==0:
                                label_result.insert("",'end', values=(i[0], i[1],"Abs"), iid = my_id, tag=('even',)) 
                            else:
                                label_result.insert("",'end', values=(i[0], i[1],"Abs"), iid = my_id, tag=('odd',)) 
                            count += 1
                        except:
                            pass  
                    else:
                        pass

                        
            mydb.commit()

           
    
    def cal():

        mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="aumas"
            )
        cursor = mydb.cursor()

        for log in logs:
            pass
        
        query = """ SELECT DISTINCT Course_title from {table_name} """.format(table_name = log)
        cursor.execute(query)
        result = cursor.fetchall()
        c_option_course = []
        for column in result:
            for i in column:
                c_option_course.append(i)

        # query_dep = """ SELECT DISTINCT Department from {table_name} """.format(table_name = log)
        # cursor.execute(query_dep)
        # result_dep = cursor.fetchall()
        # c_option_dep = []
        # for column in result_dep:
        #     for i in column:
        #         c_option_dep.append(i)
       
        global frame_cal
        frame_cal= Frame(root,width=frame_search_width, height=height, bg="white")
        frame_cal.place(x=340,y=0)

        label_title = Label(frame_cal, text="Search Records", font=(10), bg="white", fg="green")
        label_title.place(x = 8, y= 10)

        label_line1 = Label(frame_cal, text="", bg="green")
        label_line1.place(x = 0, y= 40, width=frame_search_width, height=5)

        label_line2 = Label(frame_cal, text="", bg="green")
        label_line2.place(x = 250, y= 40, width=5, height=frame_search_height)

        label_date = Label(frame_cal, text="Course:",fg="white", bg="green")
        label_date.place(x = 50, y= 80)

        clicked = StringVar()
        options = c_option_course
        global sum_course
        sum_course = ttk.Combobox (frame_cal, values =options, textvariable = clicked)
        sum_course.place(x=50, y= 110, width=100, height=50)

        label_dep = Label(frame_cal, text="Department",fg="white", bg="green")
        label_dep.place(x = 50, y= 180)

        clicked = StringVar()
        options = ["Computer Science"]
        global sum_dep
        sum_dep =ttk.Combobox (frame_cal, values =options, textvariable = clicked)
        sum_dep.place(x=50, y= 210, width=100, height=50)

        btn_sum = Button(frame_cal, text="View", bg="green", fg="white", command=lambda:query_cal())
        btn_sum.place(x = 50, y = 280, height=50, width=100)

        global label_sum_result
        label_sum_result = Label(frame_cal, text="", bg="green")
        label_sum_result.place(x = 270, y= 40, width=730, height=frame_search_height)

        frame_result= Frame(frame_cal,width=frame_view_width, height=height, bg="green")
        frame_result.place(x=280,y=40)

        

        global tree_result_sum
        columns = ("Full Name","Matric Number", "Week 1", "Week 2", "Week 3", "Week 4", "Week 5","Week 6","Week 7","Week 8","Week 9","Week 10","Week 11","Week 12","Week 13","Week 14","Week 15")
        tree_result_sum = ttk.Treeview(frame_result,columns = columns, show="headings", style="mystyle.Treeview")
        tree_result_sum.place(x = 30, y= 40, width= 650,  height = 550)
        tree_result_sum.column("#0", width=10)
        tree_result_sum.column("Full Name", width=150)
        tree_result_sum.column("Matric Number", width=100, anchor = CENTER)
        tree_result_sum.column("Week 1", width=70, anchor = CENTER)
        tree_result_sum.column("Week 2", width=70, anchor = CENTER)
        tree_result_sum.column("Week 3", width=70, anchor = CENTER)
        tree_result_sum.column("Week 4", width=70, anchor = CENTER)
        tree_result_sum.column("Week 5", width=70, anchor = CENTER)
        tree_result_sum.column("Week 6", width=70, anchor = CENTER)
        tree_result_sum.column("Week 7", width=70, anchor = CENTER)
        tree_result_sum.column("Week 8", width=70, anchor = CENTER)
        tree_result_sum.column("Week 9", width=70, anchor = CENTER)
        tree_result_sum.column("Week 10", width=70, anchor = CENTER)
        tree_result_sum.column("Week 11", width=70, anchor = CENTER)
        tree_result_sum.column("Week 12", width=70, anchor = CENTER)
        tree_result_sum.column("Week 13", width=70, anchor = CENTER)
        tree_result_sum.column("Week 14", width=70, anchor = CENTER)
        tree_result_sum.column("Week 15", width=70, anchor = CENTER)
        tree_result_sum.heading("#0", text = "S/N")
        tree_result_sum.heading("Full Name", text = "Full Name")
        tree_result_sum.heading("Matric Number", text = "Matric Number")
        tree_result_sum.heading("Week 1", text = "Week 1")
        tree_result_sum.heading("Week 2", text = "Week 2")
        tree_result_sum.heading("Week 3", text = "Week 3")
        tree_result_sum.heading("Week 4", text = "Week 4")
        tree_result_sum.heading("Week 5", text = "Week 5")
        tree_result_sum.heading("Week 6", text = "Week 6")
        tree_result_sum.heading("Week 7", text = "Week 7")
        tree_result_sum.heading("Week 8", text = "Week 8")
        tree_result_sum.heading("Week 9", text = "Week 9")
        tree_result_sum.heading("Week 10", text = "Week 10")
        tree_result_sum.heading("Week 11", text = "Week 11")
        tree_result_sum.heading("Week 12", text = "Week 12")
        tree_result_sum.heading("Week 13", text = "Week 13")
        tree_result_sum.heading("Week 14", text = "Week 14")
        tree_result_sum.heading("Week 15", text = "Week 15")

        scrollbar = ttk.Scrollbar(frame_result, orient="horizontal", command=tree_result_sum.xview)
        tree_result_sum.configure(xscrollcommand=scrollbar.set)
        scrollbar.place(x = 30, y= 580, width= 650)

        style =ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(15))
        style.configure("mystyle.Treeview.Heading",font=(20))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        
    
        tree_result_sum.tag_configure('even', background="white")
        tree_result_sum.tag_configure('odd', background="grey", foreground="white")

       
        

    def query_cal():
        mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="aumas"
            )
        cursor = mydb.cursor()

        dcourse =sum_course.get().upper()
        ddep = sum_dep.get().upper()
       
        for item in tree_result_sum.get_children():
            tree_result_sum.delete(item)

        Control_query_avail = """SELECT DISTINCT Matric_num FROM attendance WHERE Course= %s 
        AND Department=%s"""
        val1=(dcourse, ddep)
        cursor.execute(Control_query_avail,val1)
        results = cursor.fetchall()
        avail_matric = []
        matrics = []
        for j in results:
            for a in j:
                avail_matric.append(a)
            mydb.commit()
        Control_query_matric = """SELECT DISTINCT Full_Name, Matric_Num FROM students"""
        cursor.execute(Control_query_matric)
        resulted = cursor.fetchall()
        
        if avail_matric == []:
            pop_up()
        else:
            count =0
            dates=[]
            id_list =[]
            for i in resulted:
                matrics.append(i[1])
                column_id = i[1]
                Control_query_date = """SELECT DISTINCT Mdate FROM attendance"""
                cursor.execute(Control_query_date)
                date_result = cursor.fetchall()
                for date_in_result in date_result:
                    dates.append(date_in_result)
                if count % 2==0:
                    tree_result_sum.insert("",'end', values=(i[0], i[1],"","","","","","","","","","", ), iid = column_id,tags= ('even',))
                    id_list.append(column_id)
                else:
                    tree_result_sum.insert("",'end', values=(i[0], i[1],"","","","","","","","","",""), iid=column_id,tags= ('odd',))
                    id_list.append(column_id)
                count += 1
        
        nom = 0
        col = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
        save_matric = []
        for date_list in dates:
            for cols in col:
                try:
                    Control_query_m = """SELECT DISTINCT Matric_num FROM attendance WHERE Mdate=%s"""
                    val_date=(date_list[nom],)
                    cursor.execute(Control_query_m, val_date)
                    dates = cursor.fetchall()

                    for pre_date in dates:
                        for pre in pre_date:
                            save_matric.append(pre)
                    
                    for item in tree_result_sum.get_children():
                        for saved in save_matric:
                            if item == saved:
                                tree_result_sum.set(item,cols, u"\u2705")                               
                except:
                    pass    
                nom += 1
                if nom == 15:
                    nom = 0
            

        mydb.commit()            
        
   


    def view():
        mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="aumas"
            )
        cursor = mydb.cursor()

        for log in logs:
            pass
        
        query = """ SELECT DISTINCT Course_title from {table_name} """.format(table_name = log)
        cursor.execute(query)
        result = cursor.fetchall()
        c_option_course = []
        for column in result:
            for i in column:
                c_option_course.append(i)


        query_date = """ SELECT DISTINCT Mdate from attendance """
        cursor.execute(query_date)
        result_date = cursor.fetchall()
        c_option_date = []
        for column in result_date:
            for i in column:
                c_option_date.append(i)

       
        mydb.commit()
        mydb.close()
        

        global frame_view
        frame_view= Frame(root,width=frame_view_width, height=height, bg="white")
        frame_view.place(x=340,y=0)

        label_title = Label(frame_view, text="View Records", font=(10), bg="white", fg="green")
        label_title.place(x = 8, y= 10)

        label_line1 = Label(frame_view, text="", bg="green")
        label_line1.place(x = 0, y= 40, width=frame_view_width, height=5)

        label_line2 = Label(frame_view, text="", bg="green")
        label_line2.place(x = 250, y= 40, width=5, height=frame_view_height)
 
        label_date = Label(frame_view, text="Date:",fg="white", bg="green")
        label_date.place(x = 50, y= 80)

        clicked = StringVar()
        options = c_option_date
        global view_drop_date
        view_drop_date = ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_date.place(x=50, y= 110, width=100, height=50)

        label_dep = Label(frame_view, text="Department",fg="white", bg="green")
        label_dep.place(x = 50, y= 180)

        clicked = StringVar()
        options = ["Computer Science"]
        global view_drop_dep
        view_drop_dep =ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_dep.place(x=50, y= 210, width=100, height=50)

        label_course = Label(frame_view, text="Course Code:",fg="white", bg="green")
        label_course.place(x = 50, y= 280)

        clicked = StringVar()
        options = c_option_course
        global view_drop_course
        view_drop_course = ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_course.place(x=50, y= 310, width=100, height=50)

        
        btn_search = Button(frame_view, text="View", bg="green", fg="white", command=lambda: query_view())
        btn_search.place(x = 50, y = 460, height=50, width=100)

        frame_result= Frame(frame_view,width=frame_view_width, height=height, bg="green")
        frame_result.place(x=280,y=40)

        global label_result
        
        label_result = ttk.Treeview(frame_result, style="mystyle.Treeview")
        label_result['columns']= ("Full Name", "Matric Number", "Status")
        label_result.column("#0", width=10)
        label_result.column("Full Name", width=200)
        label_result.column("Matric Number", width=100, anchor = CENTER)
        label_result.column("Status", width=100)
        label_result.place(x = 40, y= 40, width= 600,  height = 500)
        label_result.heading("#0", text = "")
        label_result.heading("Full Name", text = "Full Name")
        label_result.heading("Matric Number", text = "Matric Number")
        label_result.heading("Status", text = "Status")

        style =ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(12))
        style.configure("mystyle.Treeview.Heading",font=(13))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
    
        label_result.tag_configure('even', background="white", foreground="black")
        label_result.tag_configure('odd', background="grey", foreground="white")


        # btn_print = Button(frame_result, text="Print", width=6, height=2)
        # btn_print.place(x= 520, y =550)

        # btn_save= Button(frame_result, text="Save", width=6, height=2, command=lambda:save())
        # btn_save.place(x= 540, y =550)

        # def save():
        #     f = open(f'{idate}.txt', "w")
        #     for i in imatrics:
        #         f.writelines(i)
        #     f.close()
        #     messagebox.showinfo("INFO","Data Saved Successfully")
        


    def check_card():

        try:
            reader = nfc.Reader()
            try:
                time.sleep(3)
                reader.connect()
                card_info=reader.get_uid()
            except:  
                messagebox.showerror("Error","Card Not Placed on Reader")
                pass     
        except:
            messagebox.showerror("Error","Connect NFC Reader")
        try:    
            entry_card.config(text=card_info)
        except Exception as e:
            pass

        mydb = mysql.connector.connect(
                host = "localhost",
                user= "root",
                password = "",
                port= 3306,
                database="aumas"
                )
        cursor = mydb.cursor()
        
        card_det = entry_card.cget("text")
        query_all="""SELECT Full_Name,Matric_Num, Department, Level FROM students WHERE Card_Code=%s"""
        val = (card_det,)
        cursor.execute(query_all, val)
        result = cursor.fetchall()

        e1 = entry_edit_name .get()
        e2 = entry_edit_matric .get()
        e3 = entry_edit_dep.get()
        e4 = entry_edit_level.get()

        for i in result:
            if e1 == "" and e2 == "" and e3 == "" and e4 == "":
                # entry_edit_name.delete()
                entry_edit_name.insert(0, i[0])
                entry_edit_matric.insert(0, i[1])
                entry_edit_dep.insert(0, i[2])
                entry_edit_level.insert(0, i[3])
            else:
                entry_edit_name.delete(0, END)
                entry_edit_matric.delete(0, END)
                entry_edit_dep.delete(0, END)
                entry_edit_level.delete(0, END)

                entry_edit_name.insert(0, i[0])
                entry_edit_matric.insert(0, i[1])
                entry_edit_dep.insert(0, i[2])
                entry_edit_level.insert(0, i[3])

    def submit_info():

        name=entry_edit_name.get().upper()
        matric =entry_edit_matric.get()
        dep=entry_edit_dep.get().upper()
        level=entry_edit_level.get().upper()

        mydb = mysql.connector.connect(
                host = "localhost",
                user= "root",
                password = "",
                port= 3306,
                database="aumas"
                )
        cursor = mydb.cursor()
        card_det = entry_card.cget("text")

        if name =="" and matric =="" and dep =="" and level =="":
            pop_up()
        else:
            update_query="""UPDATE students
                            SET 
                            Full_Name = %s,Matric_Num = %s,Department = %s,Level = %s
                            WHERE 
                            Card_Code = %s
                            """
            vals = (name,matric,dep,level, card_det)
            cursor.execute(update_query, vals)
            mydb.commit()
            pop_up_success()

    def edit():
        global frame_edit
        frame_edit= Frame(root,width=frame_search_width, height=height, bg="white")
        frame_edit.place(x=340,y=0)

        label_title = Label(frame_edit, text="Search Records", font=(10), bg="white", fg="green")
        label_title.place(x = 8, y= 10)

        label_line1 = Label(frame_edit, text="", bg="green")
        label_line1.place(x = 0, y= 40, width=frame_search_width, height=5)

        label_line2 = Label(frame_edit, text="", bg="green")
        label_line2.place(x = 250, y= 40, width=5, height=frame_search_height)

        label_p = Label(frame_edit, text="Card Code:", bg="white", fg="green", font=(10))
        label_p.place(x=40, y=90)

        global entry_card
        entry_card = Label(frame_edit, font=(10), bg="black", fg="white")
        entry_card.place(x = 40, y = 120,width= 180, height=50)

        btn_read = Button(frame_edit, text="Read", bg="green", fg="white", font=(10), command=lambda:check_card())
        btn_read.place(x=40, y= 190, width=180, height=50)

        frame_editup= Frame(frame_edit,width=frame_view_width, height=height, bg="green")
        frame_editup.place(x=280,y=40)

        label_p1 = Label(frame_editup, text="Name:", bg="green", fg="white", font=(10))
        label_p1.place(x=40, y=50)

        global entry_edit_name
        entry_edit_name = Entry(frame_editup, font=(10))
        entry_edit_name.place(x = 40, y = 80,width= 500, height=50)

        label_p2 = Label(frame_editup, text="Matric Number", bg="green", fg="white", font=(10))
        label_p2.place(x=40, y=150)

        global entry_edit_matric
        entry_edit_matric = Entry(frame_editup, font=(10))
        entry_edit_matric.place(x = 40, y = 180,width= 500, height=50)

        label_p3 = Label(frame_editup, text="Department", bg="green", fg="white", font=(10))
        label_p3.place(x=40, y=250)

        global entry_edit_dep
        entry_edit_dep = Entry(frame_editup, font=(10))
        entry_edit_dep.place(x = 40, y = 280,width= 500, height=50)

        label_p4 = Label(frame_editup, text="Level:", bg="green", fg="white", font=(10))
        label_p4.place(x=40, y=350)

        global entry_edit_level
        entry_edit_level = Entry(frame_editup, font=(10))
        entry_edit_level.place(x = 40, y = 380,width= 500, height=50)


        btn_submit = Button(frame_editup, text="Save Changes", bg="white", fg="green", font=(10), command=lambda:submit_info())
        btn_submit.place(x=40, y= 470, width=500, height=50)
        
    
    def settings():
        global frame_set
        frame_set= Frame(root,width=frame_search_width, height=height, bg="white")
        frame_set.place(x=340,y=0)

        label_title = Label(frame_set, text="Search Records", font=(10), bg="white", fg="green")
        label_title.place(x = 8, y= 10)

        label_line1 = Label(frame_set, text="", bg="green")
        label_line1.place(x = 0, y= 40, width=frame_search_width, height=5)

        label_line2 = Label(frame_set, text="", bg="green")
        label_line2.place(x = 250, y= 40, width=5, height=frame_search_height)

        btn_pass = Button(frame_set, text="Change Password", bg="green", fg="white", font=(10))
        btn_pass.place(x=40, y= 90, width=180, height=50)

        frame_setup= Frame(frame_set,width=frame_view_width, height=height, bg="green")
        frame_setup.place(x=280,y=40)

        label_p1 = Label(frame_setup, text="Old Password", bg="green", fg="white", font=(10))
        label_p1.place(x=40, y=50)

        global entry_set
        entry_set = Entry(frame_setup, font=(10))
        entry_set.place(x = 40, y = 80,width= 500, height=50)

        label_p2 = Label(frame_setup, text="New Password", bg="green", fg="white", font=(10))
        label_p2.place(x=40, y=150)

        global entry_set_newpass
        entry_set_newpass = Entry(frame_setup, font=(10))
        entry_set_newpass.place(x = 40, y = 180,width= 500, height=50)

        label_p3 = Label(frame_setup, text="Email", bg="green", fg="white", font=(10))
        label_p3.place(x=40, y=250)

        global entry_set_email
        entry_set_email = Entry(frame_setup, font=(10))
        entry_set_email.place(x = 40, y = 280,width= 500, height=50)

        btn_submit = Button(frame_setup, text="Save Changes", bg="white", fg="green", font=(10), command=lambda:set_settings())
        btn_submit.place(x=40, y= 350, width=180, height=50)

        def set_settings():
            mydb = mysql.connector.connect(
                host = "localhost",
                user= "root",
                password = "",
                port= 3306,
                database="aumas"
                )
            cursor = mydb.cursor()

            old_pass = entry_set.get()
            old_password =old_pass.lower()
            new_password = entry_set_newpass.get().lower()
            email =entry_set_email.get().lower()


            if old_password == "" and new_password == "":
                pop_up()
            elif old_password == new_password:
                messagebox.showwarning("Warning","Passwords Are The Same")
            else:
                set_query ="""SELECT Password FROM lecturers WHERE Password=%s"""
                val=(old_password,)
                cursor.execute(set_query, val)
                result = cursor.fetchall()
                if result == []:
                    messagebox.showerror("Error","Password Not Registered")
                else:
                    for i in result:
                        for j in i:
                            if old_password == j:
                                update_query="""UPDATE lecturers
                                SET 
                                Password = %s
                                WHERE 
                                Password = %s
                                """
                                vals = (new_password, old_password)
                                cursor.execute(update_query, vals)
                                mydb.commit()
                                pop_up_success()




    mydb.close()  
   
    
    root.mainloop()





open_page()
root.mainloop()