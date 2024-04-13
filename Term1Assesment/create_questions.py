from tkinter import *
import random as rand



class Question:
    def __init__(self, question, difficulty, type_of_question, root, answer, ans1=None, ans2=None, ans3=None):
        self.question = question
        self.difficulty = difficulty
        self.type_of_question = type_of_question
        self.root = root
        self.answer = answer
        self.ans1 = ans1
        self.ans2 = ans2
        self.ans3 = ans3
    
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
    all_questions = [Question("123123213", 2, 'multi', root, "Right", "Wrong1", "Wrong2", "Wrong3")]
    print(all_questions)
    
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    e.destroy()
    f.destroy()
    g.destroy()
    
    give_question(all_questions)


def multiple_choice(Self):
    
    
    print(Self.question)
    question_lbl = Label(Self.root, text=Self.question)
    question_lbl.place(relx=0.5, rely=0.3, anchor='center')
    
    group = IntVar()
    
    answer_1 = Radiobutton(Self.root, text="Option 1", variable=group, value=1)
    answer_1.place(relx=0.2, rely=0.6, anchor='center')
    
    answer_2 = Radiobutton(Self.root, text="Option 2", variable=group, value=2)
    answer_2.place(relx=0.4, rely=0.6, anchor='center')
    
    answer_3 = Radiobutton(Self.root, text="Option 3", variable=group, value=3)
    answer_3.place(relx=0.6, rely=0.6, anchor='center')
    
    answer_4 = Radiobutton(Self.root, text="Option 4", variable=group, value=4)
    answer_4.place(relx=0.8, rely=0.6, anchor='center')
    
    radio_list = [answer_1, answer_2, answer_3, answer_4]
    answer_list = [Self.answer, Self.ans1, Self.ans2, Self.ans3]

    for i in range(4):
        random1_num = rand.randint(0, len(radio_list) - 1)
        random2_num = rand.randint(0, len(answer_list) - 1)
        radio_btn = radio_list.pop(random1_num)
        temp_answer = answer_list.pop(random2_num)
        radio_btn.config(text=f"{temp_answer}")
        
        
    
def fill_blank():
    pass

def rank_order():
    pass


def give_question(all_questions):
    random_num = rand.randint(0, len(all_questions) - 1)
    question = all_questions.pop(random_num)
    question.create_page()

    print(all_questions)



