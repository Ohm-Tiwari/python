#Generates a random quiz with questions and answers
# 7-12-22 

import random

#Quiz dates
capitals={
    'Alabama': 'Montgomery','Alaska': 'Juneau','Arizona':'Phoenix',
    'Arkansas':'Little Rock','California': 'Sacramento','Colorado':'Denver',
    'Connecticut':'Hartford','Delaware':'Dover','Florida': 'Tallahassee',
    'Georgia': 'Atlanta','Hawaii': 'Honolulu','Idaho': 'Boise',
    'Illinios': 'Springfield','Indiana': 'Indianapolis','Iowa': 'Des Monies',
    'Kansas': 'Topeka','Kentucky': 'Frankfort','Louisiana': 'Baton Rouge',
    'Maine': 'Augusta','Maryland': 'Annapolis','Massachusetts': 'Boston',
    'Michigan': 'Lansing','Minnesota': 'St. Paul','Mississippi': 'Jackson',
    'Missouri': 'Jefferson City','Montana': 'Helena','Nebraska': 'Lincoln',
    'Neveda': 'Carson City','New Hampshire': 'Concord','New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck','Ohio': 'Columbus','Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem','Pennsylvania': 'Harrisburg','Rhode Island': 'Providence',
    'South Carolina': 'Columbia','South Dakoda': 'Pierre','Tennessee': 'Nashville',
    'Texas': 'Austin','Utah': 'Salt Lake City','Vermont': 'Montpelier',
    'Virginia': 'Richmond','Washington': 'Olympia','West Virginia': 'Charleston',
    'Wisconsin': 'Madison','Wyoming': 'Cheyenne'}

#Creates quiz & answerkey files
for quizNum in range(35):
    quizFile = open(f' capitalsquiz{quizNum + 1}.txt','w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    #writes header for quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1}')
    quizFile.write('\n\n')

    # Shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    #Loops through states. Makes questions
    for questionNum in range(50):
        #gets right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #writes question
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"  {'ABCD'[i]}. { answerOptions[i]}")
            quizFile.write('\n')

        # Write answer key to file
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
        quizFile.close()
        answerKeyFile.close()



