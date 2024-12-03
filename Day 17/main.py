# class User:
#     def __init__(self, id, username): # Class constructor with attributes
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0


#     def follow(self, user): # Method
#         user.followers += 1
#         self.following +=1


# user_1 = User("111","yoyoyoyuiyo")
# user_2 = User("112","yoyofbhafdvskjhbyoyuiyo")

# user_1.follow(user_2)

# print(user_1.following)
# print(user_2.followers)
# print("change")

from question import Question
from data import question_data
from quiz_brain import quiz_brain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = quiz_brain(question_bank)
while quiz.still_has_question():
    quiz.next_question()