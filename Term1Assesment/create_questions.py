import tkinter as tk
import random as rand


class Question:
    def __init__(self, question_text, difficulty, type_of_question, root, answer, choices=None):
        self.question_text = question_text
        self.difficulty = difficulty
        self.type_of_question = type_of_question
        self.root = root
        self.answer = answer
        self.choices = choices
  
    def __str__(self) -> str:
        return F"Question Text: {self.question_text}"
    
    def get_question_type(self):
        if self.type_of_question == 'multi':
            return multiple_choice(self)
        
        elif self.type_of_question == 'fill':
            return fill_blank()
        
        else:
            return rank_order()

    def create_page(self):
        self.get_question_type()

def main(root, a, b, c, d, e, f, g):
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

    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    e.destroy()
    f.destroy()
    g.destroy()
    
    give_question(all_questions)


def multiple_choice(question):
    
    question_lbl = tk.Label(question.root, text=question.question_text)
    question_lbl.place(relx=0.5, rely=0.3, anchor='center')
    
    group = tk.IntVar()
    group.set(0)
    
    answer_1 = tk.Radiobutton(question.root, text="Option 1", variable=group, value=1, indicatoron = 1)
    answer_1.place(relx=0.2, rely=0.6, anchor='center')
    
    answer_2 = tk.Radiobutton(question.root, text="Option 2", variable=group, value=2, indicatoron = 1)
    answer_2.place(relx=0.4, rely=0.6, anchor='center')
    
    answer_3 = tk.Radiobutton(question.root, text="Option 3", variable=group, value=3, indicatoron = 1)
    answer_3.place(relx=0.6, rely=0.6, anchor='center')
    
    answer_4 = tk.Radiobutton(question.root, text="Option 4", variable=group, value=4, indicatoron = 1)
    answer_4.place(relx=0.8, rely=0.6, anchor='center')
    
    radio_list = [answer_1, answer_2, answer_3, answer_4]

    for _ in range(4):
        random1_num = rand.randint(0, len(radio_list) - 1)
        random2_num = rand.randint(0, len(question.choices) - 1)
        radio_btn = radio_list.pop(random1_num)
        temp_answer = question.choices.pop(random2_num)
        radio_btn.config(text=f"{temp_answer}")
        
        
    
def fill_blank():
    pass

def rank_order():
    pass


def give_question(all_questions):
    random_num = rand.randint(0, len(all_questions) - 1)
    question = all_questions.pop(random_num)
    question.create_page()



