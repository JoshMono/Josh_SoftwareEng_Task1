import tkinter as tk
from tkinter import messagebox
from user_menu import create_user_interface
import json

class User():
    def __init__(self, nesa, f_name, l_name, password, mark, taken_test):
        self.nesa = nesa
        self.f_name = f_name
        self.l_name = l_name
        self.password = password
        self.mark = mark
        self.taken_test = taken_test
      
def main_menu(root):
    title_lbl = tk.Label(root, text="Software Engineering Test", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')

    login_btn = tk.Button(root, text="Login", command=lambda: login(login_btn, create_btn, title_lbl, root))
    create_btn = tk.Button(root, text="Create", command=lambda: create_account(login_btn, create_btn, title_lbl, root))

    login_btn.place(relx=0.4, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')
    create_btn.place(relx=0.6, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')

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
        
    def back_form():
        title_lbl.destroy()
        nesa_lbl.destroy()
        nesa_input.destroy()
        password_input.destroy()
        password_lbl.destroy()
        login_btn.destroy()
        hide_show_btn.destroy()
        back_btn.destroy()
        main_menu(root)
    
    
    title_lbl = tk.Label(root, text="Login", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    
    back_btn = tk.Button(root, text="Back", command=lambda: back_form())
    back_btn.place(relx=0.4, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')

    nesa_lbl = tk.Label(root, text="NESA") 
    password_lbl = tk.Label(root, text="Password")
    
    nesa_input = tk.Entry(root)
    password_input = tk.Entry(root, show="*")
    hide_show_btn = tk.Button(root, background='white', command=lambda: show(), text="Show" ,bg='white')

    nesa_input.place(relx=0.5, rely=0.5, relwidth=0.31, relheight=0.08, anchor='center')
    password_input.place(relx=0.5, rely=0.6, relwidth=0.31, relheight=0.08, anchor='center')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.075, relheight=0.08, anchor='center')

    login_btn = tk.Button(root, text="Login", command=lambda: check_login())
    login_btn.place(relx=0.6, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')
    
    nesa_lbl.place(relx=0.3, rely=0.5, relwidth=0.11, relheight=0.08, anchor='e')
    password_lbl.place(relx=0.3, rely=0.6, relwidth=0.11, relheight=0.08, anchor='e')
    
    def check_login():
        try:
            if password_input.get() != ''  and nesa_input != '':
                with open("Task1_Results.txt", "r") as file1:
                    data = file1.readline()
                    dict = json.loads(data)
            
                username_password_correct = False
                current_user = None
                
                for i in dict:
                    if i["nesa"] == nesa_input.get() and i["password"] == password_input.get():
                        username_password_correct = True
                        current_user = i
                        break
            
                if username_password_correct:
                    title_lbl.destroy()
                    nesa_lbl.destroy()
                    nesa_input.destroy()
                    password_input.destroy()
                    password_lbl.destroy()
                    login_btn.destroy()
                    hide_show_btn.destroy()
                    back_btn.destroy()

                    create_user_interface(root, current_user)
            
        
                else:
                    tk.messagebox.showwarning("Info", "Your NESA id or password is incorrect")
            else:
                tk.messagebox.showwarning("Info", "You need to fill out all of the forms")
        except Exception as e:
            print(e)

            tk.messagebox.showerror("Error", "There was an error logging you in try creating an account")


# main(root, title_lbl, nesa_lbl, password_lbl, nesa_input, password_input, submit_btn, hide_show_btn)
    

def create_account(login_btn, create_btn, title_lbl, root):
    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()
    
    def back_form():
        title_lbl.destroy()
        nesa_lbl.destroy()
        nesa_input.destroy()
        password_lbl.destroy()
        password_input.destroy()
        f_name_input.destroy()
        f_name_lbl.destroy()
        l_name_input.destroy()
        l_name_lbl.destroy()
        submit_data_btn.destroy()
        hide_show_btn.destroy()
        back_btn.destroy()
        main_menu(root)

    back_btn = tk.Button(root, text="Back", command=lambda: back_form())
    back_btn.place(relx=0.4, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')

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
    
    submit_data_btn = tk.Button(root, text="Sumbit", command=lambda: create_account())
    submit_data_btn.place(relx=0.6, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')

    

    def create_account():
        current_user = {
        "nesa": nesa_input.get(),
         "f_name": f_name_input.get(),
         "l_name": l_name_input.get(),
         "password": password_input.get(),
         "marks": [],
         "taken_test": False
        }
        
        if nesa_input.get() == '' or f_name_input.get() == '' or f_name_input.get() == '' or password_input.get() == '':
            tk.messagebox.showwarning("Info", "All fields must be filled")
            
        elif nesa_input.get().isdigit():
            try:
                with open("Task1_Results.txt", "r") as file1:
                    data = file1.readline()
            
                if data == '':
                    with open("Task1_Results.txt", "w") as file1:
                        file1.write(json.dumps([current_user]))
                        
                    title_lbl.destroy()
                    nesa_lbl.destroy()
                    nesa_input.destroy()
                    password_lbl.destroy()
                    password_input.destroy()
                    f_name_input.destroy()
                    f_name_lbl.destroy()
                    l_name_input.destroy()
                    l_name_lbl.destroy()
                    submit_data_btn.destroy()
                    hide_show_btn.destroy()
                    back_btn.destroy()
                    create_user_interface(root, current_user)
                    
                else:
                    dict = json.loads(data)
                    all_ready_in_database = False
                    for i in dict:
                        if i["nesa"] == current_user["nesa"]:
                            all_ready_in_database = True
                            
                        if all_ready_in_database == True:
                            break
                    
                    if all_ready_in_database == False:
                        dict.append(current_user)
                        json_data = json.dumps(dict)
                        with open("Task1_Results.txt", "w") as file1:
                            file1.write(json_data)

                        user = User(current_user["nesa"], current_user["f_name"], current_user["l_name"], current_user["password"], current_user["marks"], current_user["taken_test"])
                        title_lbl.destroy()
                        nesa_lbl.destroy()
                        nesa_input.destroy()
                        password_lbl.destroy()
                        password_input.destroy()
                        f_name_input.destroy()
                        f_name_lbl.destroy()
                        l_name_input.destroy()
                        l_name_lbl.destroy()
                        submit_data_btn.destroy()
                        hide_show_btn.destroy()
                        back_btn.destroy()
                        create_user_interface(root, current_user)
                        
                    else:
                        tk.messagebox.showwarning("Info", "Your NESA id is already in use")
            except:
                with open("Task1_Results.txt", "w") as file1:
                    file1.write(json.dumps([current_user]))
                    title_lbl.destroy()
                    nesa_lbl.destroy()
                    nesa_input.destroy()
                    password_lbl.destroy()
                    password_input.destroy()
                    f_name_input.destroy()
                    f_name_lbl.destroy()
                    l_name_input.destroy()
                    l_name_lbl.destroy()
                    submit_data_btn.destroy()
                    hide_show_btn.destroy()
                    back_btn.destroy()
                    create_user_interface(root, current_user)
        
        else:
            tk.messagebox.showwarning("Info", "Your NESA id can only be numbers")

    def show():
        hide_show_btn.config(command=lambda:hide(), text="Hide")   
        password_input.config(show="")

    def hide():
        hide_show_btn.config(command=lambda:show(), text="Show")   
        password_input.config(show="*")

    
    