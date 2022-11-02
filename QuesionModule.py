from ast import Add
from site import addsitepackages
from unittest import result


def AddStory(index : int, story : list, time : float, last : bool, choice : str, result):
    QuestionTable[index] = {"story" : story, "time" : time, "last" : last, "choice" : choice, "result" : result}

QuestionTable = {}

SpecialStrings = ["CHANGENAME", "TEAM"]

AddStory(1, ["Je bent geteleporteerd naar een andere dimensie.", "Je bent in schok en ziet een boze pokemon naar je toe rennen.", "Je wilt wegrennen", "maar je ziet ineens 3 pokeballen."], 
2.5, False, "Kies je pokemon:", {"a" : ["Charmander", 2], "b" : ["Bulbasaur", 2], "c" : ["Squirtle", 2]})

AddStory(2, ["Je gooid je pokebal en CHANGENAME komt eruit.", "CHANGENAME heeft de pokemon heel erg gewond gemaakt."], 
2.5, False, "Wat ga je doen met de pokemon:", {"a" : ["Spaar de pokemon", 3], "b" : ["Maak de pokemon af", 4]})

AddStory(3, ["Je hebt de Pokemon gespaard.", "Het blijkt een Rattata te zijn", "Maar Rattata is heel erg gewond"], 2.5, False, "Neem je de Rattata mee naar de stad: ", {"a" : ["Ja", 5], "b" : ["Nee", 4]})

AddStory(4, ["Je besuluit om met TEAM naar de stad te gaan", "Onderweg zie je een velle licht schijnen", "TEAM worden er bang van."], 1.5, False, "Wat doe je: ", {"a" : ["Blijf waar je bent", 6], "b" : ["Volg het licht", 7]})

AddStory(5, ["Je gaat met TEAM naar de Stad toe.", "Je loopt naar de Pokemon Center en geneesd je Pokemons", "Na het genezen van je pokemons", "Zie je een velle licht schijnen"], 
2.5, False, "Wat doe je:", {"a" : ["Volg het licht", 7], "b" : ["Blijf waar je bent", 8]})

AddStory(6, ["Het velle licht verdwijnd", "TEAM gedraagd zig weer normaal", "Maar CHANGENAME wilt dat je naar een andere richting loopt"], 1.5, False, 
"Volg je CHANGENAME of ga je richting de stad:", {"a" : ["Volg CHANGENAME", 11], "b" : ["Ga richting de stad", 12]})

AddStory(7, ["Je besluit het licht te volgen", "en uit het licht komt Arceus", "Arceus zegt: 'USERNAME, jij hebt de eerste test doorstaan", "daarom kan je mij nu zien", "maar ik voel dat je onzeker bent.", "Dus je hebt een keuze.'"], 
1.5, False, "Wil je doorgaan:", {"a" : ["Ja, ik wil doorgaan", 10], "b" : ["Nee, ik wil nu weg", 9]})

AddStory(8, ["Het licht gaat uiteindelijk weg", "en je TEAM kalmeerd", "Je ziet daarna een poster van een gym battle", "en je wilt meedoen"], 1.5, 
False, "Je weet niet waar de Gym is:", {"a" : ["Ga zoeken naar de Gym", 15], "b" : ["Ga je pokemons TEAM trainen", 16]})

# 9 is ENDING
AddStory(9, ["USERNAME, Jij hebt ervoor gekozen om weg te gaan", "Wij respecteren je keuze en ga je nu naar huis teleporteren."], 2.5, 
True, "USERNAME word terug getelporteerd naar huis", "GIVE UP ENDING")

AddStory(10, ["Arceus is blij dat je doorgaat", "Maar voordat je weg gaat", "Geeft Arcues je meer tijd om te trainen en vechten", "En Zegt Arcues dat je doel is om de gym meester te verslaan", "Als je hebt gewonnen kan je weer terug naar huis"], 1.5, 
False, "Wat wil je doen:", {"a" : ["Je pokemons trainen", 13], "b" : ["Meteen naar de gym gaan", 14]})

AddStory(11, ["Je volg CHANGENAME en je ziet een Gym", "CHANGENAME wilt dat je mee gaat doen"], 1.5, 
False, "Doe je mee aan de GYM", {"a" : ["ja, ik doe mee", 17], "b" : ["nee, ik doe niet mee", 18]})

# 12 ENDING
AddStory(12, None, None, True, "Je tijd is om en word geteleporteerd naar huis", "TIME OUT ENDING")

# 13 ENDING
AddStory(13, None, None, True, "Je pokemons evolueren en verslaan de Gym\nen je wordt getelporteerd naar huis", "DEFEAT GYM ENDING")

# 14 ENDING
AddStory(14, ["Je gaat naar de gym en je vecht tegen Giovanni", "Je pokemons zijn te zwak om te winnen"], 1.5, True, "Je verliesd de battle omdat je niet getraind hebt\nen wordt vernietigd noor Arcues", "WORST ENDING")

# 15 ENDING
AddStory(15, None, None, True, "Je probeerd te zoeken naar de Gym\nmaar je kan het niet vinden\nje tijd is om en je wordt terug gestuurd naar huis", "KEEP SEARCHING ENDING")

# 16 ENDING
AddStory(16, None, None, True, "Je tijd is om\n dus je wordt getelporteerd naar huis", "TIME OUT ENDING")

AddStory(17, ["Je besluit mee te doen met de Gym", "Maar ineens hoor je een stem", "Het is van Arceus", "Arcues Zegt dat als je wint je naar huis kan gaan", "Maar als je verliesd wordt je vernietd", "Maar als je nu opgeevd ga je ook naar huis","Maar je familie wordt vernietgd"], 
1, False, "Wat ga je doen:", {"a" : ["Geef op", 19], "b" : ["Doorgaan", 20], "c" : ["Jezelf opoveren"]})

# 18 ENDING
AddStory(18, None, None, True, "Je bent te bang om te vechten\n Dus je gaat uit de Gym\nen wordt terug getelporteerd naar huis", "RETREAT ENDING")

# 19 ENDING
AddStory(19, None, None, True, "Je geeft op\nen Arcues stuurt je terug naar huis", "GIVE UP ENDING")

# 20 ENDING
AddStory(20, None, None, True, "Na een lange gevecht verlies je\n en je wordt vernietgd noor Arcues", "ALMOST THERE ENDING")

# 21 ENDING
AddStory(21, None, None, True, "Je probeerd te vluchten en wordt vernietgd door Arceus\nmaar je familie is veilig", "SACRIFICE ENDING")