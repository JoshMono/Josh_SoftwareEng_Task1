import tkinter as tk
import random as rand
from tkinter import messagebox



class Question:
    def __init__(self, question_text, difficulty, type_of_question, root, answer, choices=None):
        self.question_text = question_text
        self.difficulty = difficulty
        self.type_of_question = type_of_question
        self.root = root
        self.answer = answer
        self.choices = choices
    
    def get_question_type(self):
        if self.type_of_question == 'multi':
            return multiple_choice, self
        
        elif self.type_of_question == 'fill':
            return fill_blank, self
        
        else:
            return rank_order()

def main(root, current_user):
    all_questions = []
    from questions_data import QUESTIONS
    for question in QUESTIONS:
        q = Question(
            question_text=question.get('question_text'),
            difficulty=question.get('difficulty'),
            type_of_question=question.get('type_of_question'),
            root=root,
            answer=question.get('answer'),
            choices=question.get('choices')
            )
        all_questions.append(q)
        
    score = 0
    total = 0
    
    for question in all_questions:
        total += question.difficulty
        
    score_lbl = tk.Label(root, text=f"{score}/{total}")
    score_lbl.place(relx=0.9, rely=0.1)
    
    
    
    give_question(all_questions, current_user, score, total, score_lbl, root)


def multiple_choice(question, all_questions, current_user, score, total, score_lbl):
    
    question_lbl = tk.Label(question.root, text=question.question_text, font=30)
    question_lbl.place(relx=0.5, rely=0.3, anchor='center')
    
    group = tk.StringVar()
    
    answer_1 = tk.Radiobutton(question.root, text="Option 1", variable=group, tristatevalue=0)
    answer_1.place(relx=0.2, rely=0.6, anchor='center')
    
    answer_2 = tk.Radiobutton(question.root, text="Option 2", variable=group, tristatevalue=0)
    answer_2.place(relx=0.4, rely=0.6, anchor='center')
    
    answer_3 = tk.Radiobutton(question.root, text="Option 3", variable=group, tristatevalue=0)
    answer_3.place(relx=0.6, rely=0.6, anchor='center')
    
    answer_4 = tk.Radiobutton(question.root, text="Option 4", variable=group, tristatevalue=0)
    answer_4.place(relx=0.8, rely=0.6, anchor='center')
    
    radio_list = [answer_1, answer_2, answer_3, answer_4]
    temp_choices = question.choices.copy()

    for _ in range(4):
        random1_num = rand.randint(0, len(radio_list) - 1)
        random2_num = rand.randint(0, len(temp_choices) - 1)
        radio_btn = radio_list.pop(random1_num)
        temp_answer = temp_choices.pop(random2_num)
        radio_btn.config(text=f"{temp_answer}", value=f"{temp_answer}")
        
    submit_btn = tk.Button(question.root, text="Submit", command=lambda: submit_value(question, group.get(), score, total, score_lbl))
    submit_btn.place(relx=0.5, rely=0.75, relwidth=0.11, relheight=0.08, anchor="center")
    
    def new_question(score, total, score_lbl, correct_lbl, root):
        give_question(all_questions, current_user, score, total, score_lbl, root)
        submit_btn.destroy()
        answer_1.destroy()
        answer_2.destroy()
        answer_3.destroy()
        answer_4.destroy()
        question_lbl.destroy()
        correct_lbl.destroy()
        
    def submit_value(question, selected, score, total, score_lbl):
        if selected == '':
            tk.messagebox.showwarning("Info", "You must answer the question")
            
        elif question.answer == selected:
            correct_lbl = tk.Label(question.root, text="Correct")
            correct_lbl.place(relx=0.5, rely=0.5, anchor='center')
            score += question.difficulty
            score_lbl.config(text=f"{score}/{total}")
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, correct_lbl, question.root), bg="spring green")
        
        else:
            incorrect_lbl = tk.Label(question.root, text="Incorrect")
            incorrect_lbl.place(relx=0.5, rely=0.5, anchor='center')
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, incorrect_lbl, question.root), bg="red")
            
        
    
def fill_blank(question, all_questions, current_user, score, total, score_lbl):
    title_lbl = tk.Label(question.root, text="Fill in the Blank", font=30)
    title_lbl.place(relx=0.5, rely=0.2, anchor='center')
    
    question_lbl = tk.Label(question.root, text=f"Question: {question.question_text}")
    question_lbl.place(relx=0.5, rely=0.4, anchor='center')
    
    answer_field = tk.Entry(question.root)
    answer_field.place(relx=0.5, rely=0.6, relwidth=0.12, anchor='center')
    
    submit_btn = tk.Button(question.root, text="Submit", command=lambda: submit_value(question, score, total, score_lbl))
    submit_btn.place(relx=0.5, rely=0.75, relwidth=0.11, relheight=0.08, anchor="center")
    
    def submit_value(question, score, total, score_lbl):
        if answer_field.get() == '':
            tk.messagebox.showwarning("Info", "You must answer the question")
        elif question.answer == answer_field.get().lower():
            correct_lbl = tk.Label(question.root, text="Correct")
            correct_lbl.place(relx=0.5, rely=0.5, anchor='center')
            score += question.difficulty
            score_lbl.config(text=f"{score}/{total}")
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, correct_lbl, question.root), bg="spring green")
        else:
            incorrect_lbl = tk.Label(question.root, text="Incorrect")
            incorrect_lbl.place(relx=0.5, rely=0.5, anchor='center')
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, incorrect_lbl, question.root), bg="red")
            
    def new_question(score, total, score_lbl, correct_lbl, root):
        give_question(all_questions, current_user, score, total, score_lbl, root)
        submit_btn.destroy()
        answer_field.destroy()
        question_lbl.destroy()
        title_lbl.destroy()
        correct_lbl.destroy()

def rank_order():
    pass


def give_question(all_questions, current_user, score, total, score_lbl, root):
    if len(all_questions) == 0:
        score_lbl.config(text=f"{score}/{total}")
        current_user['marks'].append(score)
        
        import json
        with open("Task1_Results.txt", "r") as file1:
            data = file1.readline()
            
        my_dict = json.loads(data)

        for i in my_dict:
            if i['nesa'] == current_user['nesa']:
                i['marks'] = current_user['marks']
                
        with open("Task1_Results.txt", "w") as file1:
            file1.write(json.dumps(my_dict))

        from user_menu import create_user_interface
        create_user_interface(root, current_user)
    else:
        score_lbl.config(text=f"{score}/{total}")
        random_num = rand.randint(0, len(all_questions) - 1)
        question = all_questions.pop(random_num)
        func, self = question.get_question_type()
        func(self, all_questions, current_user, score, total, score_lbl)



