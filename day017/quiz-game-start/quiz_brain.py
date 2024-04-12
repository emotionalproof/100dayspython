# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO:  checking if we're at the end of the quiz

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        q_text = current_q.text
        correct_answer = current_q.answer
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False)?  \n")
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Boom")
            self.score += 1
        else:
            print("Suck it")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def final_score(self):
        return f"Your final score was: {self.score}/{len(self.question_list)}"