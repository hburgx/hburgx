from gettext import install
import random

import colorama
import pip
from questions import detroit_become_human
from questions import fallout_4
from questions import star_wars


class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer.strip().upper()
        self.correct_letter = self.correct_answer[0]

    def check_answer(self, user_answer):
        return user_answer.strip().upper() == self.correct_letter


class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = []
        self.load_questions()

    def load_questions(self):
        all_question_data = (
            detroit_become_human.questions
            + fallout_4.questions
            + star_wars.questions
        )
        for data in all_question_data:
            question = Question(
                data["question"],
                data["options"],
                data["correct_answer"],
            )
            self.questions.append(question)

    def choose_questions(self, number_of_questions):
        shuffled_questions = self.questions[:]
        random.shuffle(shuffled_questions)
        return shuffled_questions[:number_of_questions]

    def ask_question(self, question):
        print()
        print(question.text)

        for option in question.options:
            print(option)

        player_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        while player_answer not in ["A", "B", "C", "D"]:
            print("Please enter a valid option (A, B, C, or D).")
            player_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        if question.check_answer(player_answer):
            self.score += 1
            print("Correct!")
        else:
            print("Wrong The correct answer was " + question.correct_answer + ".")

    def play(self):
        number_of_rounds = 5
        selected_questions = self.choose_questions(number_of_rounds)

        print("============= Welcome to the Quiz Game! =============")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("You will be asked a series of questions. Try to answer them correctly!")
        print("Enter A, B, C, or D for your answer. Good luck!")

        round_number = 1
        for question in selected_questions:
            print()
            print("Round " + str(round_number) + " out of " + str(number_of_rounds))
            self.ask_question(question)
            print("Your current score is: " + str(self.score))
            round_number += 1

        print()
        print("Game Over")
        print("Final Score: " + str(self.score) + " out of " + str(number_of_rounds))

from colorama import Fore, init

init()
print(Fore.GREEN + "")

if __name__ == "__main__":
    game = QuizGame()
    game.play()