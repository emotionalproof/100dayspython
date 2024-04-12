from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


def create_questions(question_data):
    for q in question_data:
        new_q = Question(text=q["question"], answer=q["correct_answer"])
        question_bank.append(new_q)


create_questions(question_data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(quiz.final_score())