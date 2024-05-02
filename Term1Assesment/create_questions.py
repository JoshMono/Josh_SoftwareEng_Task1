from os import replace
from re import S
import select
import tkinter as tk
from tkinter.ttk import Treeview
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
            return rank_order, self

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
        
    score_header_lbl = tk.Label(root, text=f"Score")
    score_header_lbl.place(relx=0.76, rely=0.1, anchor='center')

    question_num_header_lbl = tk.Label(root, text=f"Question")
    question_num_header_lbl.place(relx=0.9, rely=0.1, anchor='center')

    score_lbl = tk.Label(root, text=f"{score}/{total}")
    score_lbl.place(relx=0.76, rely=0.15, anchor='center')
    
    question_num_lbl = tk.Label(root, text=f"20/20")
    question_num_lbl.place(relx=0.9, rely=0.15, anchor='center')
    
    give_question(all_questions, current_user, score, total, score_lbl, root, 0, question_num_lbl, len(all_questions), score_header_lbl, question_num_header_lbl)


def multiple_choice(question, all_questions, current_user, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
    
    if question.question_text.__contains__('$'):
        number_answer = rand.randint(0,255)
        answer = str(format(number_answer, '#010b')).replace("0b", "")
        question.question_text = question.question_text.replace("$", str(number_answer))
        question.choices = []
        for i in range(3):
            temp_ans = ""
            a = True
            while a == True:
                for _ in range(8):
                    temp_num = rand.randint(0,1)
                    temp_ans += str(temp_num)
                if temp_ans == answer or temp_ans in question.choices:
                    print(temp_ans)
                    temp_ans = ""
                else:
                    a = False
                    question.choices.append(temp_ans)

        question.choices.append(answer)
        question.answer = answer

    question_lbl = tk.Label(question.root, text=question.question_text, font=30)
    question_lbl.place(relx=0.5, rely=0.3, anchor='center')
    
    group = tk.StringVar()
    
    answer_1 = tk.Radiobutton(question.root, text="Option 1", variable=group, tristatevalue=0)
    answer_1.place(relx=0.5, rely=0.4, anchor='center')
    
    answer_2 = tk.Radiobutton(question.root, text="Option 2", variable=group, tristatevalue=0)
    answer_2.place(relx=0.5, rely=0.48, anchor='center')
    
    answer_3 = tk.Radiobutton(question.root, text="Option 3", variable=group, tristatevalue=0)
    answer_3.place(relx=0.5, rely=0.56, anchor='center')
    
    answer_4 = tk.Radiobutton(question.root, text="Option 4", variable=group, tristatevalue=0)
    answer_4.place(relx=0.5, rely=0.64, anchor='center')
    
    mark_lbl = tk.Label(question.root, text=f"Difficulty")
    mark_lbl.place(relx=0.1, rely=0.1, anchor='center')
    mark_score_lbl = tk.Label(question.root, text=f"{question.difficulty}/3")
    mark_score_lbl.place(relx=0.1, rely=0.15, anchor='center')

    radio_list = [answer_1, answer_2, answer_3, answer_4]
    temp_choices = question.choices.copy()

    for _ in range(4):
        random1_num = rand.randint(0, len(radio_list) - 1)
        random2_num = rand.randint(0, len(temp_choices) - 1)
        radio_btn = radio_list.pop(random1_num)
        temp_answer = temp_choices.pop(random2_num)
        radio_btn.config(text=f"{temp_answer}", value=f"{temp_answer}")
        
    submit_btn = tk.Button(question.root, text="Submit", command=lambda: submit_value(question, group.get(), score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl))
    submit_btn.place(relx=0.5, rely=0.75, relwidth=0.11, relheight=0.08, anchor="center")
    
    def new_question(score, total, score_lbl, correct_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
        give_question(all_questions, current_user, score, total, score_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl)
        submit_btn.destroy()
        answer_1.destroy()
        answer_2.destroy()
        answer_3.destroy()
        answer_4.destroy()
        question_lbl.destroy()
        mark_lbl.destroy()
        mark_score_lbl.destroy()
        correct_lbl.destroy()
        
    def submit_value(question, selected, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
        if selected == '':
            tk.messagebox.showwarning("Info", "You must answer the question")
            
        elif question.answer == selected:
            correct_lbl = tk.Label(question.root, text="Correct")
            correct_lbl.place(relx=0.5, rely=0.22, anchor='center')
            score += question.difficulty
            score_lbl.config(text=f"{score}/{total}")
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, correct_lbl, question.root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl), bg="spring green")
        
        else:
            incorrect_lbl = tk.Label(question.root, text="Incorrect")
            incorrect_lbl.place(relx=0.5, rely=0.22, anchor='center')
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, incorrect_lbl, question.root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl), bg="red")
            
        
    
def fill_blank(question, all_questions, current_user, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
    
    if question.question_text.__contains__('$$$$'):
        new_binary_num = ""
        for i in range(4):
            temp_num = rand.randint(0,1)
            new_binary_num += str(temp_num)
        question.question_text = question.question_text.replace("$$$$", new_binary_num)
        question.answer = str(int(new_binary_num, 2))
        

    title_lbl = tk.Label(question.root, text="Fill in the Blank", font=30)
    title_lbl.place(relx=0.5, rely=0.2, anchor='center')
    
    question_lbl = tk.Label(question.root, text=f"Question: {question.question_text}")
    question_lbl.place(relx=0.5, rely=0.4, anchor='center')
    
    answer_field = tk.Entry(question.root)
    answer_field.place(relx=0.5, rely=0.6, relwidth=0.12, anchor='center')
    
    mark_lbl = tk.Label(question.root, text=f"Difficulty")
    mark_lbl.place(relx=0.1, rely=0.1, anchor='center')
    mark_score_lbl = tk.Label(question.root, text=f"{question.difficulty}/3")
    mark_score_lbl.place(relx=0.1, rely=0.15, anchor='center')
    
    submit_btn = tk.Button(question.root, text="Submit", command=lambda: submit_value(question, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl))
    submit_btn.place(relx=0.5, rely=0.75, relwidth=0.11, relheight=0.08, anchor="center")
    
    

    def submit_value(question, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
        if answer_field.get() == '':
            tk.messagebox.showwarning("Info", "You must answer the question")
        elif question.answer == answer_field.get().lower():
            correct_lbl = tk.Label(question.root, text="Correct")
            correct_lbl.place(relx=0.5, rely=0.5, anchor='center')
            score += question.difficulty
            score_lbl.config(text=f"{score}/{total}")
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, correct_lbl, question.root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl), bg="spring green")
        else:
            incorrect_lbl = tk.Label(question.root, text="Incorrect")
            incorrect_lbl.place(relx=0.5, rely=0.5, anchor='center')
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, incorrect_lbl, question.root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl), bg="red")
            
    def new_question(score, total, score_lbl, correct_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
        give_question(all_questions, current_user, score, total, score_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl)
        submit_btn.destroy()
        answer_field.destroy()
        question_lbl.destroy()
        mark_lbl.destroy()
        mark_score_lbl.destroy()
        title_lbl.destroy()
        correct_lbl.destroy()

def rank_order(question, all_questions, current_user, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
    title_lbl = tk.Label(question.root, text="Rank in Order", font=30)
    title_lbl.place(relx=0.5, rely=0.2, anchor='center')
    
    question_lbl = tk.Label(question.root, text=f"Question: {question.question_text}")
    question_lbl.place(relx=0.5, rely=0.28, anchor='center')
    
    choice_tree = Treeview(question.root, selectmode='browse')
    choice_tree.place(relx=0.5, rely=0.7, relwidth=0.34, anchor='center')
    choice_tree['columns'] = ("1")
    choice_tree['show'] = 'headings'
    choice_tree.column('1', anchor='w', width=30)
    choice_tree.heading('1', text='Rank Order', anchor='center')

    mark_lbl = tk.Label(question.root, text=f"Difficulty")
    mark_lbl.place(relx=0.1, rely=0.1, anchor='center')
    mark_score_lbl = tk.Label(question.root, text=f"{question.difficulty}/3")
    mark_score_lbl.place(relx=0.1, rely=0.15, anchor='center')
    
    choices_list = question.choices.copy()
    
    for choice in question.choices:
       num = rand.randint(0, len(choices_list) - 1)
       ran_choice = choices_list.pop(num)
       choice_tree.insert("", 'end', values=[f"{ran_choice}"])
       
    move_up_btn = tk.Button(question.root, text="Move Up", command=lambda: move_up())
    move_up_btn.place(relx=0.2, rely=0.55, relwidth=0.15, relheight=0.08, anchor='center')
    
    move_down_btn = tk.Button(question.root, text="Move Down", command=lambda: move_down())
    move_down_btn.place(relx=0.2, rely=0.75, relwidth=0.15, relheight=0.08, anchor='center')
    
    submit_btn = tk.Button(question.root, text="Submit", command=lambda: submit(score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl))
    submit_btn.place(relx=0.8, rely=0.65, relwidth=0.15, relheight=0.08, anchor='center')

    def move_up():
        try:
            selected = choice_tree.selection()
            choice_tree.move(selected, choice_tree.parent(selected), choice_tree.index(selected) - 1)
        except:
            tk.messagebox.showwarning("Info", "You must select a row")
        
    def move_down():
        try:
            selected = choice_tree.selection()
            choice_tree.move(selected, choice_tree.parent(selected), choice_tree.index(selected) + 1)
        except:
            tk.messagebox.showwarning("Info", "You must select a row")
    
    def new_question(score, total, score_lbl, correct_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
        title_lbl.destroy()
        question_lbl.destroy()
        choice_tree.destroy()
        correct_lbl.destroy()
        move_down_btn.destroy()
        move_up_btn.destroy()
        submit_btn.destroy()
        mark_lbl.destroy()
        mark_score_lbl.destroy()
        give_question(all_questions, current_user, score, total, score_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl)

    def submit(score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
        all_choices = choice_tree.get_children()
        answer_choices = question.choices
        num = 0
        correct = True
        for i in all_choices:
            item = choice_tree.item(i)
            text = item.get('values')[0]
            a = answer_choices[num]
            if str(text) != a:
                correct = False
                break
            num += 1
            
        if correct:
            correct_lbl = tk.Label(question.root, text="Correct")
            correct_lbl.place(relx=0.2, rely=0.65, anchor='center')
            score += question.difficulty
            score_lbl.config(text=f"{score}/{total}")
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, correct_lbl, question.root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl), bg="spring green")
        else: 
            incorrect_lbl = tk.Label(question.root, text="Incorrect")
            incorrect_lbl.place(relx=0.2, rely=0.65, anchor='center')
            submit_btn.config(text="Next", command=lambda: new_question(score, total, score_lbl, incorrect_lbl, question.root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl), bg="red")

def give_question(all_questions, current_user, score, total, score_lbl, root, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl):
    if len(all_questions) == 0:
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


        header_lbl = tk.Label(root, text="Summary", font=40)
        header_lbl.place(relx=0.5, rely=0.3, anchor="center")
        
        question_num_header_lbl.destroy()
        question_num_lbl.destroy()
        
        score_header_lbl.place(relx=0.3, rely=0.43, anchor="center")
        score_lbl.place(relx=0.3, rely=0.5, anchor="center")
        score_lbl.config(text=f"{score}/{total}")
        
        percent_header_lbl = tk.Label(root, text="Percent")
        percent_lbl = tk.Label(root, text=f"{round(score/40*100)}%")
        percent_header_lbl.place(relx=0.5, rely=0.43, anchor="center")
        percent_lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        
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

        grade_header_lbl = tk.Label(root, text="Grade")
        grade_lbl = tk.Label(root, text=f"{get_grade(score)}")
        grade_header_lbl.place(relx=0.7, rely=0.43, anchor="center")
        grade_lbl.place(relx=0.7, rely=0.5, anchor="center")
        # from user_menu import create_user_interface
        # create_user_interface(root, current_user)
        meun_btn = tk.Button(root, text="Menu", command=lambda: back_to_menu(root, current_user))
        meun_btn.place(relx=0.5, rely=0.63, anchor="center")

        def back_to_menu(root, current_user):
            header_lbl.destroy()
            meun_btn.destroy()
            score_header_lbl.destroy()
            score_lbl.destroy()
            percent_header_lbl.destroy()
            percent_lbl.destroy()
            grade_header_lbl.destroy()
            grade_lbl.destroy()
            from user_menu import create_user_interface
            create_user_interface(root, current_user)    
            
    else:
        question_num += 1
        score_lbl.config(text=f"{score}/{total}")
        question_num_lbl.config(text=f"{question_num}/{amount_of_questions}")
        random_num = rand.randint(0, len(all_questions) - 1)
        question = all_questions.pop(random_num)
        func, self = question.get_question_type()
        func(self, all_questions, current_user, score, total, score_lbl, question_num, question_num_lbl, amount_of_questions, score_header_lbl, question_num_header_lbl)



