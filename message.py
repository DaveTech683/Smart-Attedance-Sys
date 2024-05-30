from tkinter import *


def pop_up():
    root = Tk()
    root.geometry('150x100')
    root.title("ERROR")
    root.attributes('-topmost',True)
    root.config(bg="red")
    root.eval('tk::PlaceWindow . center')

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        pass

    Label_pass= Label(root, text="Empty", bg="red",fg="white", font=(10))
    Label_pass.place(x=45, y=35)

    root.after(1500, lambda:root.destroy())



    root.mainloop()

def pop_up_success():
    root = Tk()
    root.geometry('150x100')
    root.title("ERROR")
    root.attributes('-topmost',True)
    root.config(bg="green")
    root.eval('tk::PlaceWindow . center')

    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        pass

    Label_pass= Label(root, text="Change Saved", bg="green",fg="white", font=(10))
    Label_pass.place(x=20, y=35)

    root.after(1500, lambda:root.destroy())



    root.mainloop()