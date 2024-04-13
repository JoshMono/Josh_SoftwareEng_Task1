from tkinter import *
from PIL import ImageTk, Image
from create_questions import main




def login(login_btn, create_btn, title_lbl, root):
    
    
    
    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()

    hide213 = True
    
    def show():
        hide_show_btn.config(command=lambda:hide(), text="Hide")   
        password_input.config(show="")

    def hide():
        hide_show_btn.config(command=lambda:show(), text="Show")   
        password_input.config(show="*")
        
        
    
    
    title_lbl = Label(root, text="Login", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    
    nesa_lbl = Label(root, text="Nesa") 
    password_lbl = Label(root, text="Password")
    
    nesa_input = Entry(root)
    password_input = Entry(root, show="*")
    hide_show_btn = Button(root, background='white', command=lambda: show(), text="Show" ,bg='white')

    nesa_input.place(relx=0.5, rely=0.5, relwidth=0.31, relheight=0.08, anchor='center')
    password_input.place(relx=0.5, rely=0.6, relwidth=0.31, relheight=0.08, anchor='center')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.075, relheight=0.08, anchor='center')

    submit_btn = Button(root, text="Login", command=lambda: main(root, title_lbl, nesa_lbl, password_lbl, nesa_input, password_input, submit_btn, hide_show_btn))
    submit_btn.place(relx=0.3, rely=0.8, relwidth=0.11, relheight=0.08, anchor='e')
    
    nesa_lbl.place(relx=0.3, rely=0.5, relwidth=0.11, relheight=0.08, anchor='e')
    password_lbl.place(relx=0.3, rely=0.6, relwidth=0.11, relheight=0.08, anchor='e')
    
def create_account():
    pass