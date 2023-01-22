class QuizBrain:

    def __init__(self, q_list):
        self.question_li = q_list

    def next_question(self):
        current_question = self.question_li
