from data import question_list as ql
class Quiz:
    def __init__(self, ql):
        self.question_number = 0
        self.score = 0
        self.question_list = ql

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question['text']} (True/False): ").lower()
            self.check_answer(user_answer, current_question['answer'])


        else:
            print("No more questions. Your quiz is over!")

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


quiz = Quiz(ql)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz completed. Your final score is: {quiz.score}/{len(quiz.question_list)}")
