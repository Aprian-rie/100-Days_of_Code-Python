from qn_model import Question
from data import question_data
from quiz_brain import QuizBrain
# import random

question_bank = []
difficulty = input("Select The difficulty easy, medium or hard")
if difficulty == "easy":
    for qns in question_data:
        qn_object = Question(qns["question"], qns["correct_answer"])
        question_bank.append(qn_object)
elif difficulty == "medium":
    for qns in question_data:
        qn_object = Question(qns["question"], qns["correct_answer"])
        question_bank.append(qn_object)
elif difficulty == "hard":
    for qns in question_data:
        qn_object = Question(qns["question"], qns["correct_answer"])
        question_bank.append(qn_object)
# print(question_bank)

# random_object = (random.choice(question_bank))
# print(random_object.text)
# print(random_object.answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.qn_number}")