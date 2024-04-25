import tkinter as tk
from tkinter.ttk import Treeview
from create_questions import main

def create_user_interface(root, current_user):
    welcome_lbl = tk.Label(root, text=f"Welcome {current_user['f_name']}", font=40)
    welcome_lbl.place(relx=0.05, rely=0.08, anchor='w')
    
    mark_list = Treeview(root, selectmode='browse')
    mark_list.place(relx=0.97, rely=0.50, relwidth=0.32, relheight=0.95, anchor='e')
    mark_list['columns'] = ("1", "2")
    mark_list['show'] = 'headings'
    mark_list.column('1', anchor='w', width=30)
    mark_list.heading('1', text='Attempt', anchor='center')
    mark_list.column('2', anchor='w', width=30)
    mark_list.heading('2', text='Marks', anchor='center')
    

    i=1
    for mark in current_user["marks"]:
       mark_list.insert("", 'end', values=(i, f"{round(mark/20*100)}%"))
       i+=1
       

    start_test_btn = tk.Button(root, text="Start Test", command=lambda: run_questions(root, current_user))
    start_test_btn.place(relx=0.05, rely=0.18)
    
    def run_questions(root, current_user):
        welcome_lbl.destroy()
        mark_list.destroy()
        start_test_btn.destroy()
        main(root, current_user)
        