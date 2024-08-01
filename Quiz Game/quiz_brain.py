class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question_text} (True/False): ").lower()
        if user_answer == "t":
            user_answer = "True"
        elif user_answer == "f":
            user_answer = "False"
        elif user_answer == "stop":
            return True
        else:
            print("\n---> You entered a wrong letter! please type either 't' or 'f'.\n")
        self.check_answer(user_answer, current_question.question_answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            print(" ✔️ You got it right! 😃")
            self.score += 1
        else:
            print(" ❌ That's wrong! 🙃")
        print(f"    The correct answer is: {current_answer}")
        print(f"    Your current score is: {self.score}/{self.question_number}\n")
