from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
question_bank=[]
for question in question_data:
    question_text=question['question']
    question_answer=question['correct_answer']
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
    
quiz=Quiz_brain(question_bank)

while  quiz.still_has_questions():
    quiz.next_question() 

print("you've completed the quize")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")
