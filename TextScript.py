from ast import In, Starred
from TextModule import Question
import os

question_index = 1

ended = False

os.system('cls')

Starter = None
Team = None
username = input("Wat is jouw naam: ")

os.system('cls')

while ended == False:
    if question_index <= 1:
        new_index, starter, team = Question(question_index, "", username, [])

        Starter = starter
        Team = team
    else:
        new_index, starter, team = Question(question_index, Starter, username, Team)

    if new_index != 0:
        os.system('cls')

        question_index = new_index
    else:
        break
