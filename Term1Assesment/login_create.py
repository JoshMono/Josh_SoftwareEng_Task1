from email import message
from mailbox import Message
import tkinter as tk
from tkinter import messagebox
from create_questions import main
import json

class User():
    def __init__(self, f_name, l_name, password, mark, taken_test):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password
        self.mark = mark
        self.taken_test = taken_test
               

def login(login_btn, create_btn, title_lbl, root):
    
    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()
    
    def show():
        hide_show_btn.config(command=lambda:hide(), text="Hide")   
        password_input.config(show="")

    def hide():
        hide_show_btn.config(command=lambda:show(), text="Show")   
        password_input.config(show="*")
        
        
    
    
    title_lbl = tk.Label(root, text="Login", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    
    nesa_lbl = tk.Label(root, text="NESA") 
    password_lbl = tk.Label(root, text="Password")
    
    nesa_input = tk.Entry(root)
    password_input = tk.Entry(root, show="*")
    hide_show_btn = tk.Button(root, background='white', command=lambda: show(), text="Show" ,bg='white')

    nesa_input.place(relx=0.5, rely=0.5, relwidth=0.31, relheight=0.08, anchor='center')
    password_input.place(relx=0.5, rely=0.6, relwidth=0.31, relheight=0.08, anchor='center')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.075, relheight=0.08, anchor='center')

    login_btn = tk.Button(root, text="Login", command=lambda: test())
    login_btn.place(relx=0.3, rely=0.8, relwidth=0.11, relheight=0.08, anchor='e')
    
    nesa_lbl.place(relx=0.3, rely=0.5, relwidth=0.11, relheight=0.08, anchor='e')
    password_lbl.place(relx=0.3, rely=0.6, relwidth=0.11, relheight=0.08, anchor='e')
    
    def check_login():
        pass

# main(root, title_lbl, nesa_lbl, password_lbl, nesa_input, password_input, submit_btn, hide_show_btn)
    

def create_account(login_btn, create_btn, title_lbl, root):
    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()
    
    title_lbl = tk.Label(root, text="Create Account", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    
    nesa_lbl = tk.Label(root, text="NESA")
    nesa_input = tk.Entry(root)
    nesa_lbl.place(relx=0.3, rely=0.3, relwidth=0.11, relheight=0.08, anchor='e')
    nesa_input.place(relx=0.5, rely=0.3, relwidth=0.31, relheight=0.08, anchor='center')
    
    f_name_lbl = tk.Label(root, text="First Name")
    f_name_input = tk.Entry(root)
    f_name_lbl.place(relx=0.3, rely=0.4, relwidth=0.13, relheight=0.08, anchor='e')
    f_name_input.place(relx=0.5, rely=0.4, relwidth=0.31, relheight=0.08, anchor='center')
    
    l_name_lbl = tk.Label(root, text="Last Name")
    l_name_input = tk.Entry(root)
    l_name_lbl.place(relx=0.3, rely=0.5, relwidth=0.13, relheight=0.08, anchor='e')
    l_name_input.place(relx=0.5, rely=0.5, relwidth=0.31, relheight=0.08, anchor='center')
    
    password_lbl = tk.Label(root, text="Password")
    password_input = tk.Entry(root, show="*")
    password_lbl.place(relx=0.3, rely=0.6, relwidth=0.13, relheight=0.08, anchor='e')
    password_input.place(relx=0.5, rely=0.6, relwidth=0.31, relheight=0.08, anchor='center')
    
    hide_show_btn = tk.Button(root, background='white', command=lambda: show(), text="Show" ,bg='white')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.075, relheight=0.08, anchor='center')
    
    submit_data_btn = tk.Button(root, text="Sumbit", command=lambda: submit_data())
    submit_data_btn.place(relx=0.4, rely=0.7,)

    

    def submit_data():
        current_user = {
        "nesa": nesa_input.get(),
         "f_name": f_name_input.get(),
         "l_name": l_name_input.get(),
         "password": password_input.get(),
         "marks": []
        }
        
        if nesa_input.get() == '' or f_name_input.get() == '' or f_name_input.get() == '' or password_input.get() == '':
            tk.messagebox.showwarning("Info", "All fields must be filled")
            
        else:
            try:
                with open("Task1_Results.txt", "r") as file1:
                    data = file1.readline()
            
                if data == '':
                    with open("Task1_Results.txt", "w") as file1:
                        file1.write(json.dumps([current_user]))
                    
                else:
                    dict = json.loads(data)
                    for i in dict:
                        if i["nesa"] != current_user["nesa"]:
                            dict.append(current_user)
                            json_data = json.dumps(dict)
                            with open("Task1_Results.txt", "w") as file1:
                                file1.write(json_data)
                        else:
                            tk.messagebox.showwarning("Info", "Your NESA id is already in use")
            except:
                with open("Task1_Results.txt", "w") as file1:
                    file1.write(json.dumps([current_user]))

    def show():
        hide_show_btn.config(command=lambda:hide(), text="Hide")   
        password_input.config(show="")

    def hide():
        hide_show_btn.config(command=lambda:show(), text="Show")   
        password_input.config(show="*")

    
    