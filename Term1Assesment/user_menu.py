from math import e
import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import messagebox
from create_questions import main
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def create_user_interface(root, current_user):
    welcome_lbl = tk.Label(root, text=f"Welcome {current_user['f_name']}", font=40)
    welcome_lbl.place(relx=0.05, rely=0.08, anchor='w')
    
    mark_list_tree = Treeview(root, selectmode='browse')
    mark_list_tree.place(relx=0.97, rely=0.50, relwidth=0.35, relheight=0.95, anchor='e')
    mark_list_tree['columns'] = ("1", "2", "3")
    mark_list_tree['show'] = 'headings'
    mark_list_tree.column('1', anchor='w', width=30)
    mark_list_tree.heading('1', text='Attempt', anchor='center')
    mark_list_tree.column('2', anchor='w', width=30)
    mark_list_tree.heading('2', text='Marks', anchor='center')
    mark_list_tree.column('3', anchor='w', width=30)
    mark_list_tree.heading('3', text='Grade', anchor='center')
    
    def get_grade(mark):
        if mark >= 40 * 0.9:
            return "A"
        
        elif mark >= 40 * 0.75:
            return "B"
        
        elif mark >= 40 * 0.60:
            return "C"

        elif mark >= 40 * 0.35:
            return "D"
        
        else:
            return "E"

    i=1
    for mark in current_user["marks"]:
       mark_list_tree.insert("", 'end', values=(i, f"{round(mark/40*100)}%", get_grade(mark)))
       i+=1
       

    start_test_btn = tk.Button(root, text="Start Test", command=lambda: run_questions(root, current_user))
    start_test_btn.place(relx=0.05, rely=0.18)
    
    quit_btn = tk.Button(root, text="Quit", command=lambda: root.destroy())
    quit_btn.place(relx=0.2, rely=0.18)
    
    i=1
    attempt_list = []
    mark_list = []
    for mark in current_user["marks"]:
        attempt_list.append(i)
        mark_list.append(mark)
        i += 1
            
    f = Figure(figsize=(5,5), dpi=80)
    a = f.add_subplot(111)
    a.plot(attempt_list,mark_list)
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().place(relx=0.06, rely=0.62, relheight=0.55, relwidth=0.55, anchor="w")
    
    marks_lbl = tk.Label(root, text=f"Marks", wraplength=1)
    marks_lbl.place(relx=0.015, rely=0.535)
    
    attemps_lbl = tk.Label(root, text=f"Attemps")
    attemps_lbl.place(relx=0.27, rely=0.905)
    
    graph_lbl = tk.Label(root, text=f"Marks Graph")
    graph_lbl.place(relx=0.24, rely=0.27)

    def run_questions(root, current_user):
        if tk.messagebox.askquestion(title="Test Agreements", message="Do you agree that this test will be your own work?") == 'yes':
            welcome_lbl.destroy()
            mark_list_tree.destroy()
            start_test_btn.destroy()
            canvas.get_tk_widget().destroy()
            marks_lbl.destroy()
            attemps_lbl.destroy()
            graph_lbl.destroy()
            quit_btn.destroy()
            main(root, current_user)
        