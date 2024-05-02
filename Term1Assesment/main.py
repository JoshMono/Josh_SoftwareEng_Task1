import tkinter as tk
from tkinter import font
import login_create


# Main function that starts the tkinter window
def __main__():
    # Creating the root which creates a window
    root = tk.Tk()
    root.geometry('450x300')

    # Adding Labels and buttons for information and navigation
    title_lbl = tk.Label(root, text="Software Engineering Test", font=20)
    
    # On click runs the login function that creates a login form
    login_btn = tk.Button(root, text="Login", command=lambda: login_create.login(login_btn, create_btn, title_lbl, root))
    
    # On click runs the create_account function that creates a form
    create_btn = tk.Button(root, text="Create", command=lambda: login_create.create_account(login_btn, create_btn, title_lbl, root))
    
    # Placing all tk widgets on the window
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')
    login_btn.place(relx=0.4, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')
    create_btn.place(relx=0.6, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')

    # Runs the tkinter mainloop which keeps the tkinter window open
    root.mainloop()

# Calls main to start program
__main__()