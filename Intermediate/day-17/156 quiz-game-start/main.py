from data import question_data
from question_model import Question
question_bank = []
for data in question_data:
    new_question = Question(question_data["text"], question_data["answer"])
    question_bank.append(new_question)
