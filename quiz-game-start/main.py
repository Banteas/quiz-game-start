from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html



question_bank = []


for item in question_data:
    question_text = html.unescape(item["question"])
    question_answer = html.unescape(item["correct_answer"])
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was: {quiz.score}/{len(question_bank)}")

