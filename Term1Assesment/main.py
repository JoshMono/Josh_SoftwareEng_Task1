import tkinter as tk
from tkinter import font
import login_create



def __main__():
    root = tk.Tk()
    root.geometry('450x300')

    title_lbl = tk.Label(root, text="Software Engineering Test", font=20)
    title_lbl.place(relx=0.5, rely=0.13, anchor='center')

    login_btn = tk.Button(root, text="Login", command=lambda: login_create.login(login_btn, create_btn, title_lbl, root))
    create_btn = tk.Button(root, text="Create", command=lambda: login_create.create_account(login_btn, create_btn, title_lbl, root))

    login_btn.place(relx=0.4, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')
    create_btn.place(relx=0.6, rely=0.5, relwidth=0.11, relheight=0.08, anchor='center')

    root.mainloop()


__main__()