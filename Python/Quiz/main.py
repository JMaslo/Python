from question_model import Question
from data import question_data

question_list = []


for one_question in question_data:
    ques_text = one_question["text"]
    ques_anwer = one_question["answer"]
    new_question = Question(ques_text, ques_anwer)
    question_list.append(new_question)





print(question_list)