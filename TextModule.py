from multiprocessing.connection import wait
from tkinter.messagebox import QUESTION
from QuesionModule import QuestionTable
from time import sleep

Starter = None

def Question(question_index):
    skip = False

    if QuestionTable[question_index]["last"] == False:
        while True:
            if skip == False:
                for dialouge in QuestionTable[question_index]["story"]:
                    print(dialouge)
                    sleep(QuestionTable[question_index]["time"])
                
            print(QuestionTable[question_index]["choice"], "\n")

            for name, options in QuestionTable[question_index]["choices"].items():
                print(name + ")", options[0])
                sleep(1)

            result = input("option: ")

            for name, options in QuestionTable[question_index]["choices"].items():
                if result.lower() == name.lower():
                    if question_index == 1:
                        Starter = options[0]
                        print("Your Starter is", Starter)
                    return options[1]
            
            print(result, "is a invalid input\n")
            sleep(1)
            skip = True
