from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    q_text = questions["text"]
    q_answer = questions["answer"]
    question = Question(q_text, q_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)
print("Welcome to The Lonasctech True or False Quiz Game!")
print("📝 Type 't' for True or 'f' for False.\n")

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}")

"""
On behalf of the entire SPE NAU Executive Committee and myself, 
I extend our heartfelt gratitude for the privilege and opportunity to serve.
 
we aim to take the organization to a greater height and ensure that all members actively 
contribute to its development and achievement of the SPE goals.  

We also seek for the members to utilize the
opportunities that we are entitled to as a registered member of SPE. 
We appreciate everyone's commitment to the growth of our chapter. 

Let's continue working together with the SPE vibes, guided by God's wisdom and directions.
We say thank you for the privilege to serve as we do our best.

Best regards,
SPE NAU EXCO 2023/2024
Anthony Udem - President
"""
