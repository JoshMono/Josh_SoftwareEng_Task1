import tkinter as tk
from tkinter import messagebox
from user_menu import create_user_interface
import json


# Runs a login form
def login(login_btn, create_btn, title_lbl, root):
    # Destroys the widgets on the previous forms
    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()
    
    # Shows the password in the entry field
    def show():
        hide_show_btn.config(command=lambda:hide(), text="Hide")   
        password_input.config(show="")

    # Hides the password in the entry field
    def hide():
        hide_show_btn.config(command=lambda:show(), text="Show")   
        password_input.config(show="*")
        
    # Destroys all the current widgets and runs __main__ to run the quiz main menu again
    def back_form():
        title_lbl.destroy()
        nesa_lbl.destroy()
        nesa_input.destroy()
        password_input.destroy()
        password_lbl.destroy()
        login_btn.destroy()
        hide_show_btn.destroy()
        back_btn.destroy()
        root.destroy()
        from main import __main__
        __main__()
    
    # Creates and places all widgets
    title_lbl = tk.Label(root, text="Login", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    
    # Runs back_form on click event
    back_btn = tk.Button(root, text="Back", command=lambda: back_form())
    back_btn.place(relx=0.4, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')

    nesa_lbl = tk.Label(root, text="NESA") 
    password_lbl = tk.Label(root, text="Password")
    
    nesa_input = tk.Entry(root)
    password_input = tk.Entry(root, show="*")
    
    # Runs show on click which shows the password in the entry field
    hide_show_btn = tk.Button(root, background='white', command=lambda: show(), text="Show" ,bg='white')

    # Placing widgets on screen
    nesa_input.place(relx=0.5, rely=0.5, relwidth=0.31, relheight=0.08, anchor='center')
    password_input.place(relx=0.5, rely=0.6, relwidth=0.31, relheight=0.08, anchor='center')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.075, relheight=0.08, anchor='center')

    login_btn = tk.Button(root, text="Login", command=lambda: check_login())
    login_btn.place(relx=0.6, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')
    
    nesa_lbl.place(relx=0.3, rely=0.5, relwidth=0.11, relheight=0.08, anchor='e')
    password_lbl.place(relx=0.3, rely=0.6, relwidth=0.11, relheight=0.08, anchor='e')
    
    # Checks database too verify if ur allowed to login
    def check_login():
        try:
            # If both the fields arn't empty then it runs
            if password_input.get() != ''  and nesa_input != '':
                # Opens the file and reads it in and converts it from a json file to a list of dictonarys
                with open("Task1_Results.txt", "r") as file1:
                    data = file1.readline()
                    dict = json.loads(data)
            
                username_password_correct = False
                current_user = None
                
                # Loops through all the values in the list and checks if your information matches any of the ones in the database
                for i in dict:
                    if i["nesa"] == nesa_input.get() and i["password"] == password_input.get():
                        username_password_correct = True
                        current_user = i
                        break
                
                # If your information matches with one in the database it destroys all the widgets and run create_user_interface
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
            
                # If it dosn't match then it shows a warning
                else:
                    tk.messagebox.showwarning("Info", "Your NESA id or password is incorrect")
                    
                # Runs if all boxes arn't filled out
            else:
                tk.messagebox.showwarning("Info", "You need to fill out all of the forms")
        except:
            # Runs when somthing crashes most likely reason for it to crash is nothing in the database
            tk.messagebox.showerror("Error", "There was an error logging you in try creating an account")


 
# Runs a create account form
def create_account(login_btn, create_btn, title_lbl, root):
    # Destroys the widgets on the previous forms
    login_btn.destroy()
    create_btn.destroy()
    title_lbl.destroy()
    
    # Shows the password in the entry field
    def show():
        hide_show_btn.config(command=lambda:hide(), text="Hide")   
        password_input.config(show="")

    # Hides the password in the entry field
    def hide():
        hide_show_btn.config(command=lambda:show(), text="Show")   
        password_input.config(show="*")

    # Destroys all the current widgets and runs __main__ to run the quiz main menu again
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
        root.destroy()
        from main import __main__
        __main__()

    # Creates widgets for form
    
    # On click runs back_form which clears this screen and returns to main menu
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
    
    # On click runs show
    hide_show_btn = tk.Button(root, background='white', command=lambda: show(), text="Show" ,bg='white')
    hide_show_btn.place(relx=0.7, rely=0.6, relwidth=0.075, relheight=0.08, anchor='center')
    
    # Creates a account on click
    submit_data_btn = tk.Button(root, text="Sumbit", command=lambda: create_account())
    submit_data_btn.place(relx=0.6, rely=0.8, relwidth=0.11, relheight=0.08, anchor='center')

    
    # Creates an account for the user
    def create_account():
        # Users information in a dictonary
        current_user = {
        "nesa": nesa_input.get(),
         "f_name": f_name_input.get(),
         "l_name": l_name_input.get(),
         "password": password_input.get(),
         "marks": [],
         "taken_test": False
        }
        
        # Checks if any fields are empty and if they are throws a warning
        if nesa_input.get() == '' or f_name_input.get() == '' or f_name_input.get() == '' or password_input.get() == '':
            tk.messagebox.showwarning("Info", "All fields must be filled")
        
        # Checks if the nesa id is a number
        elif nesa_input.get().isdigit():
            
            try:
                # Opens and imports sets data too the database
                with open("Task1_Results.txt", "r") as file1:
                    data = file1.readline()
                
                # If the database is empty it writes the current_user which is a dictonary into the database then creates the user interface
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
                    # Converts from json to list of dictonarys
                    dict = json.loads(data)
                    all_ready_in_database = False
                    
                    # Loops through all of the nesa ids in the database to check if theres two of the same
                    for i in dict:
                        if i["nesa"] == current_user["nesa"]:
                            all_ready_in_database = True
                            
                        if all_ready_in_database == True:
                            break
                    
                    # If the nesa id is unique the current_user is appened into the list of all the other users and then written to a file
                    if all_ready_in_database == False:
                        dict.append(current_user)
                        json_data = json.dumps(dict)
                        with open("Task1_Results.txt", "w") as file1:
                            file1.write(json_data)
                            
                        # Destroys all widgets and runs the user interface
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
                        # Runs if theres a duplicate nesa id
                        tk.messagebox.showwarning("Info", "Your NESA id is already in use")
            except:
                # If crashes then current user is written to the database then runs create_user_interface
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
            # Runs if nesa id isnt numbers
            tk.messagebox.showwarning("Info", "Your NESA id can only be numbers")

    

    
    