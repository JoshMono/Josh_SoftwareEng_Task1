from tkinter import *
from tkinter import font

def test():
    pass

root = Tk()
root.geometry('450x300')

title_lbl = Label(root, text="Software Engineering Test", font=20)
title_lbl.place(relx=0.5, rely=0.13, anchor='center')

login_btn = Button(root, text="Login", command=lambda: test())
create_btn = Button(root, text="Create", command=lambda: test())

login_btn.place(relx=0.4, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')
create_btn.place(relx=0.6, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')



root.mainloop()
