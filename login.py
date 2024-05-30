# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.app import MDApp
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.list import OneLineListItem
# import json
# import requests

# Builder.load_string("""
# <LoginScreen>:
#     BoxLayout:
#         orientation: 'vertical'
#         padding: 10
#         spacing: 10
#         GridLayout:
#             rows: 3
#             cols: 1
#             padding: 10
#             spacing: 10
#             row_default_height: 30
#             MDTextField:
#                 hint_text: "Email"
#                 id: usernamevalue
#             MDTextField:
#                 hint_text: "Password"
#                 id: passwordvalue
#                 password: True
#             MDRectangleFlatButton:
#                 text: 'Login'
#                 on_press: root.login_button_action()
# <FailedLoginScreen>:
#     BoxLayout:
#         orientation: 'vertical'
#         padding: 10
#         spacing: 10
#         MDLabel:
#             text: "Login Failed"
#         MDRectangleFlatButton:
#             text: 'Back To Login'
#             on_press: root.manager.current = 'login'
# <TaskScreen>:
#     MDList:
#         id: tasklist
# """)

# class FailedLoginScreen(Screen):
#     pass


# class TaskScreen(Screen):
#     def on_enter(self):
#         for i in range(20):
#             self.ids.tasklist.add_widget(
#                 OneLineListItem(text=f"Filler task {i}")
#             )


# class LoginScreen(Screen):
#     def build(self):
#         pass
 
#     def login_button_action(self):
#         url = 'https://reqres.in/api/login'
        
#         #data = json.dumps({"email": "eve.holt@reqres.in","password": "cityslicka"})
#         data = json.dumps({"email": self.ids.usernamevalue.text,"password": self.ids.passwordvalue.text})

#         response = requests.post(url, data=data, headers={'Content-Type':'application/json'})

#         userdata = json.loads(response.text)

#         if userdata.get("token"):
#             self.manager.current = 'tasklist'
#         else:
#             self.manager.current = 'failedlogin'


# class MainApp(MDApp):

#     def build(self):
#         sm = ScreenManager();
#         sm.add_widget(LoginScreen(name='login'))
#         sm.add_widget(FailedLoginScreen(name='failedlogin'))
#         sm.add_widget(TaskScreen(name='tasklist'))

#         return sm

# if __name__ == '__main__':
#     MainApp().run()

from tkinter import *



root = Tk()
root.geometry("200x200")
root.resizable(0,0)


txt = Label(root,text="X and O")
txt.place(x=80, y=10)

slt1= Button(root, command=lambda:slt_1())
slt1.place(x=30, y=40, width=40, height=40)

def slt_1():
    if slt2['text'] == ""  or slt3['text'] == "" or slt4['text'] == "":
        slt1.config(text="X")
    elif slt2['text'] == "X"  or slt3['text'] == "X" or slt4['text'] == "X":
        slt1.config(text="O")
    elif slt4['text'] == "O"  or slt4['text'] == "O" or slt4['text'] == "O":
        slt1.config(text="X")

slt2= Button(root,command=lambda:slt_2())
slt2.place(x=70, y=40, width=40, height=40)

def slt_2():
    if slt1['text'] == ""  or slt4['text'] == "" or slt3['text'] == "":
        slt2.config(text="X")
    elif slt1['text'] == "X"  or slt4['text'] == "X" or slt3['text'] == "X":
        slt2.config(text="O")
    elif slt1['text'] == "O"  or slt4['text'] == "O" or slt3['text'] == "O":
        slt2.config(text="X")


slt3= Button(root, command=lambda:slt_3())
slt3.place(x=110, y=40, width=40, height=40)

def slt_3():
    slt3.config(text="X")

slt4= Button(root, command=lambda:slt_4())
slt4.place(x=30, y=80, width=40, height=40)

def slt_4():
    slt4.config(text="X")

slt5= Button(root, command=lambda:slt_5())
slt5.place(x=70, y=80, width=40, height=40)

def slt_5():
    slt5.config(text="X")

slt6= Button(root)
slt6.place(x=110, y=80, width=40, height=40)



slt7= Button(root)
slt7.place(x=30, y=120, width=40, height=40)

slt8= Button(root)
slt8.place(x=70, y=120, width=40, height=40)

slt9= Button(root)
slt9.place(x=110, y=120, width=40, height=40)








root.mainloop()




















# print(column_id, 'column id')
       
        
        #         Control_query_date = """SELECT DISTINCT Mdate FROM attendance"""
        #         cursor.execute(Control_query_date)
        #         results = cursor.fetchall()
        #         num = 0     
        #         availing = []
        #         for j in results:
        #             for a in j:
        #                 num +=1
        #                 Control_query = """SELECT DISTINCT Matric_num FROM attendance WHERE Mdate = %s """
        #                 valing=(a,)
        #                 cursor.execute(Control_query, valing)
        #                 result = cursor.fetchall()
                        
        #                 for i in result:
        #                     for k in i:
        #                         for m in matrics:
        #                             if k == m:
        #                                 availing.append(k)
            
        # print(data_matrics, "lists")     
        # print(id_list, "column id")
        # for data in data_matrics:
        #     for id_lists in id_list:
        #         if data == id_lists:
        #             for item in tree_result_sum.get_children():
        #                 if item == data:
        #                     tree_result_sum.set(item,'2', "Present")
                        
                            
                        
                        # for item in tree_result_sum.get_children():
                        #     for avails in availing:
                                
                        #         if avails == column_id:
                        #             print('column_id', column_id)
                        #             print('avails', avails)
                        #             tree_result_sum.set(item,'2', "Present",column=column_id)
                        #         else:
                        #             pass
                    