from tkinter import *
import mysql.connector
from tkinter import messagebox, ttk
from message import pop_up
from py_acr122u import nfc
import time
from AUMAS import login


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

    mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="aumas"
            )
    cursor = mydb.cursor()


    frame_nav= Frame(root,width=frame_nav_width, height=height, bg="green")
    frame_nav.place(x=0,y=0)

    btn_view = Button(frame_nav, text="View Records >>>", font=(12), bg="green", fg="white", command=lambda: view())
    btn_view.place(x = 70, y = 90, height=50, width=180)

    btn_cal = Button(frame_nav, text="Edit Records", font=(12), bg="green", fg="white", command = lambda:edit() )
    btn_cal.place(x = 70, y = 190, height=50, width=180)

    btn_cal = Button(frame_nav, text="Calculate Attendance", font=(12), bg="green", fg="white", command = lambda:cal() )
    btn_cal.place(x = 70, y = 290, height=50, width=180)


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

        icourse = view_drop_course.get()
        global idate
        idate =view_drop_date.get()
        idep = view_drop_dep.get()
        ilevel = view_drop_level.get()

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
        AND Department=%s AND Mdate=%s AND level =%s"""
        val1=(icourse, idep, idate, ilevel)
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
        count = 0
        if resulted == []:
            pop_up()
        else:
            for i in resulted:
                for avail in avail_matric:
                    if avail in i[1]:
                        label_result.insert("",'end', values=(i[0], i[1],"Present"))
                        
                    else:
                        label_result.insert("",'end', values=(i[0], i[1],"Abs"))
                        break
            mydb.commit()

        

        
    
    def cal():
        messagebox.showinfo("INFO", "Page Currently Unavailable")
    # def query_cal():
        
    #     mydb = mysql.connector.connect(
    #         host = "localhost",
    #         user= "root",
    #         password = "",
    #         port= 3306,
    #         database="aumas"
    #         )
    #     cursor = mydb.cursor()

    #     dcourse = cal_drop_course.get()
    #     ddate =cal_drop_date.get()
    #     ddep = cal_drop_dep.get()
    #     dlevel = cal_drop_level.get()

        
    #     Control_query_cal = """SELECT COUNT(Matric_num) FROM attendance WHERE Course= %s 
    #     AND Department=%s AND Mdate=%s AND level =%s"""
    #     val2=(dcourse, ddep, ddate, dlevel)
    #     cursor.execute(Control_query_cal,val2)
    #     resulted = cursor.fetchall()
    #     global i, matrics
    #     for i in resulted:
    #         for matrics in range(len(i)):
    #             pass
    #     # label_result.config(text=i[matrics])
    #     mydb.commit()

        # SELECT Matric_num FROM attendance WHERE Course= 'PYTHON PROGRAMMING' 
        # AND Department='COMPUTER SCIENCE' AND Mdate='2023-08-09' AND level ='HND 1' IF LIMIT 10

        
        

    def view():
        mydb = mysql.connector.connect(
            host = "localhost",
            user= "root",
            password = "",
            port= 3306,
            database="aumas"
            )
        cursor = mydb.cursor()
        
        query = """ SELECT DISTINCT Course from attendance """
        cursor.execute(query)
        result = cursor.fetchall()
        c_option_course = []
        for column in result:
            for i in column:
                c_option_course.append(i)

        query_dep = """ SELECT DISTINCT Department from attendance """
        cursor.execute(query_dep)
        result_dep = cursor.fetchall()
        c_option_dep = []
        for column in result_dep:
            for i in column:
                c_option_dep.append(i)

        query_date = """ SELECT DISTINCT Mdate from attendance """
        cursor.execute(query_date)
        result_date = cursor.fetchall()
        c_option_date = []
        for column in result_date:
            for i in column:
                c_option_date.append(i)

        query_level = """ SELECT DISTINCT level from attendance """
        cursor.execute(query_level)
        result_level = cursor.fetchall()
        c_option_level = []
        for column in result_level:
            for i in column:
                c_option_level.append(i)
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
        label_date.place(x = 50, y= 60)

        clicked = StringVar()
        options = c_option_date
        global view_drop_date
        view_drop_date = ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_date.place(x=50, y= 90, width=100, height=50)

        label_dep = Label(frame_view, text="Department",fg="white", bg="green")
        label_dep.place(x = 50, y= 160)

        clicked = StringVar()
        options = c_option_dep
        global view_drop_dep
        view_drop_dep =ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_dep.place(x=50, y= 190, width=100, height=50)

        label_course = Label(frame_view, text="Course Code:",fg="white", bg="green")
        label_course.place(x = 50, y= 260)

        clicked = StringVar()
        options = c_option_course
        global view_drop_course
        view_drop_course = ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_course.place(x=50, y= 290, width=100, height=50)

        label_level = Label(frame_view, text="level:",fg="white", bg="green")
        label_level.place(x = 50, y= 350)

        clicked = StringVar()
        options = c_option_level
        global view_drop_level
        view_drop_level = ttk.Combobox (frame_view, values =options, textvariable = clicked)
        view_drop_level.place(x=50, y= 370, width=100, height=50)
        
        btn_search = Button(frame_view, text="View", bg="green", fg="white", command=lambda: query_view())
        btn_search.place(x = 50, y = 450, height=50, width=100)

        frame_result= Frame(frame_view,width=frame_view_width, height=height, bg="green")
        frame_result.place(x=280,y=40)


        global label_result
        
        label_result = ttk.Treeview(frame_result)
        label_result['columns']= ("Full Name", "Matric Number", "Status")
        label_result.column("#0", width=10)
        label_result.column("Full Name", width=200)
        label_result.column("Matric Number", width=100, anchor = CENTER)
        label_result.column("Status", width=100)
        label_result.place(x = 40, y= 40, width= 600,  height = 500)
        label_result.heading("#0", text = "S/N")
        label_result.heading("Full Name", text = "Full Name")
        label_result.heading("Matric Number", text = "Matric Number")
        label_result.heading("Status", text = "Status")


        # btn_print = Button(frame_result, text="Print", width=6, height=2)
        # btn_print.place(x= 520, y =550)

        btn_save= Button(frame_result, text="Save", width=6, height=2, command=lambda:save())
        btn_save.place(x= 540, y =550)

        def save():
            f = open(f'{idate}.txt', "w")
            for i in imatrics:
                f.writelines(i)
            f.close()
            messagebox.showinfo("INFO","Data Saved Successfully")
        


    # def read_card():
    #     try:
    #         reader = nfc.Reader()
    #         try:
    #             time.sleep(3)
    #             reader.connect()
    #             card_info=reader.get_uid()
    #         except:  
    #             messagebox.showerror("Error","Card Not Placed on Reader")
    #             pass     
    #     except:
    #         messagebox.showerror("Error","Connect The NFC Reader,\n Page Will be Closed")
    #     try:    
    #         edit_dep.config(text=card_info)
    #     except Exception as e:
    #         pass

    def edit():
        messagebox.showinfo("INFO", "This Page is Currently Unavailable")
        
    #     global frame_cal
    #     frame_cal= Frame(root,width=frame_search_width, height=height, bg="white")
    #     frame_cal.place(x=340,y=0)

    #     label_title = Label(frame_cal, text="Search Records", font=(10), bg="white", fg="green")
    #     label_title.place(x = 8, y= 10)

    #     label_line1 = Label(frame_cal, text="", bg="green")
    #     label_line1.place(x = 0, y= 40, width=frame_search_width, height=5)

    #     label_line2 = Label(frame_cal, text="", bg="green")
    #     label_line2.place(x = 250, y= 40, width=5, height=frame_search_height)

    #     label_dep = Label(frame_cal, text="Card ID:",fg="white", bg="green")
    #     label_dep.place(x = 50, y= 60)

    #     global edit_dep
    #     edit_dep = Entry(frame_cal)
    #     edit_dep.place(x=50, y= 90, width=100, height=50)

    #     btn_cal = Button(frame_cal, text="Read Card", bg="green", fg="white", command=lambda:read_card())
    #     btn_cal.place(x = 50, y = 160, height=50, width=100)

    #     btn_cal = Button(frame_cal, text="View", bg="green", fg="white", command=lambda:edit_query())
    #     btn_cal.place(x = 50, y = 260, height=50, width=100)

    #     global label_cal_result
    #     label_cal_result = Label(frame_cal, text="", bg="green")
    #     label_cal_result.place(x = 270, y= 40, width=730, height=frame_search_height)

    #     frame_result= Frame(frame_cal,width=frame_view_width, height=height, bg="green")
    #     frame_result.place(x=280,y=40)


    #     global tree_result
    #     columns = ("Full Name","Matric Numbers", "Department","Level")
    #     tree_result = ttk.Treeview(frame_result,columns = columns, show="headings")
    #     tree_result.place(x = 40, y= 40, width= 600,  height = 500)
    #     tree_result.heading("Full name", text = "Full Name")
    #     tree_result.heading("Matrc Number", text = "Matric Number")
    #     tree_result.heading("Department", text = "Department")
    #     tree_result.heading("Level", text = "Level")

    # def edit_query():

    #     editing= edit_dep.get()
    #     mydb = mysql.connector.connect(
    #         host = "localhost",
    #         user= "root",
    #         password = "",
    #         port= 3306,
    #         database="aumas"
    #         )
    #     cursor = mydb.cursor()
        
        # query = """ SELECT * from students WHERE Card_Code=%s """
        # val=(editing)
        # cursor.execute(query, val)
        # result = cursor.fetchall()
        # for column in result:
        #     for i in column:
        #         c_option_course.append(i)



    mydb.close()  
   
    
    root.mainloop()



