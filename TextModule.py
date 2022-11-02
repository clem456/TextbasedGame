from QuesionModule import QuestionTable
from time import sleep
import os

def Question(question_index, Starter, username, Team):
    skip = False

    if QuestionTable[question_index]["last"] == False:
        while True:
            if skip == False:
                if question_index == 2:
                    Team.append(Starter)
                elif question_index == 5:
                    Team.append("Rattata")

                for dialouge in QuestionTable[question_index]["story"]:
                    userdialouge = dialouge.replace("USERNAME", username)

                    if "CHANGENAME" in userdialouge:
                        newdialouge = userdialouge.replace("CHANGENAME", Starter)
                        print(newdialouge)
                    elif "TEAM" in userdialouge:
                        pokemonstr = ""

                        for number, pokemon in enumerate(Team, 1):
                            if number < len(Team) and len(Team) - number == 1:
                                pokemonstr += pokemon
                            elif number < len(Team) and len(Team) - number != 1:
                                pokemonstr += pokemon + ", "
                            elif number == len(Team) and number == 1:
                                pokemonstr = pokemon
                            elif number == len(Team) and number != 1:
                                pokemonstr += " en " + pokemon

                        newdialouge = userdialouge.replace("TEAM", pokemonstr)
                        print(newdialouge)
                    else:
                        print(userdialouge)
                    
                    sleep(QuestionTable[question_index]["time"])
            
            sentance = QuestionTable[question_index]["choice"] + "\n"

            if "CHANGENAME" in sentance:
                newsentance = sentance.replace("CHANGENAME", Starter)
                print(newsentance)
            elif "TEAM" in sentance:
                pokemonstr = ""

                for number, pokemon in enumerate(Team, 1):
                    if number < len(Team) and len(Team) - number == 1:
                        pokemonstr += pokemon
                    elif number < len(Team) and len(Team) - number != 1:
                        pokemonstr += pokemon + ", "
                    elif number == len(Team) and number == 1:
                        pokemonstr = pokemon
                    elif number == len(Team) and number != 1:
                        pokemonstr += " en " + pokemon
        
                newsentance = sentance.replace("TEAM", pokemonstr)
                print(newsentance)
            else:
                print(sentance)

            for name, options in QuestionTable[question_index]["result"].items():
                option = options[0]
                
                if "CHANGENAME" in option:
                    newoption = option.replace("CHANGENAME", Starter)
                    print(name + ")", newoption)
                elif "TEAM" in option:
                    pokemonstr = ""

                    for number, pokemon in enumerate(Team, 1):
                        if number < len(Team) and len(Team) - number == 1:
                            pokemonstr += pokemon
                        elif number < len(Team) and len(Team) - number != 1:
                            pokemonstr += pokemon + ", "
                        elif number == len(Team) and number == 1:
                            pokemonstr = pokemon
                        elif number == len(Team) and number != 1:
                            pokemonstr += " en " + pokemon

                    newoption = option.replace("TEAM", pokemonstr)
                    print(name + ")", newoption)
                else:
                    print(name + ")", option)
                sleep(1)

            result = input("option: ")

            for name, options in QuestionTable[question_index]["result"].items():
                if result.lower() == name.lower():
                    if question_index == 1:
                        Starter = options[0]
                        print("Your Starter is", Starter)
                    return options[1], Starter, Team

            os.system('cls')
            print(result, "is a invalid input\n")
            sleep(1)
            skip = True
    else:        
        print("You unlocked:", QuestionTable[question_index]["result"] + "\n")

        ending = QuestionTable[question_index]["choice"].replace("USERNAME", username)

        print(ending)

        sleep(5)

        return 0, None, None