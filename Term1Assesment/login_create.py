from tkinter import *
from PIL import ImageTk



def login(login_btn, create_btn, title_lbl, root):
    hide = True
    
    def hide_show(hide):
        print(hide)
        if hide:
            hide_show_btn.config(image=show_image)
            password_input.config(show="")
            hide = False
        else:
            hide = True

    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()
    
    title_lbl = Label(root, text="Login", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    
    nesa_lbl = Label(root, text="Nesa")
    password_lbl = Label(root, text="Password")
    
    hide_image = ImageTk.PhotoImage(file='images//eye-hide.png')
    show_image = ImageTk.PhotoImage(file='images//eye-show.png')
    
    nesa_input = Entry(root)
    password_input = Entry(root, show="*")
    hide_show_btn = Button(root, background='white', command=lambda: hide_show(hide))

    print(hide_show_btn.image_names)
    nesa_input.place(relx=0.5, rely=0.5, relwidth=0.31, relheight=0.08, anchor='center')
    password_input.place(relx=0.5, rely=0.6, relwidth=0.31, relheight=0.08, anchor='center')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.05, relheight=0.08, anchor='center')
    
    nesa_lbl.place(relx=0.3, rely=0.5, relwidth=0.11, relheight=0.08, anchor='e')
    password_lbl.place(relx=0.3, rely=0.6, relwidth=0.11, relheight=0.08, anchor='e')
    
def create_account():
    pass