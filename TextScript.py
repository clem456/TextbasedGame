from TextModule import Question

question_index = 1

ended = False

while ended == False:
    new_index = Question(question_index)

    if new_index != 0:
        question_index = new_index
    else:
        ended = True
