from pathlib import Path
import random
import sys

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

(Path.cwd() / 'result_attachments' / 'quiz').mkdir(exist_ok=True)
p1 = Path.cwd() / 'result_attachments' / 'quiz'

for quizNum in range(int(sys.argv[1])):
    quizFile = open(p1 / f'capitalsquiz{quizNum+1}.txt', mode='w')
    answerFile = open(p1 / f'capitalsquiz_answer{quizNum+1}.txt', mode='w')

    quizFile.write('Name: \n\nDate: \n\nPeriod: \n\n')
    quizFile.write((' ' * 20) + f'State Capital Quiz (Form {quizNum+1})')
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)

    for qNum in range(int(sys.argv[2])):
        correctAnswer = capitals[states[qNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'{qNum+1}. What is the capital of {states[qNum]}?\n')
        for i in range(4):
            quizFile.write(f'{"ABCD"[i]}. {answerOptions[i]}\t')
        quizFile.write('\n\n')

        answerFile.write(f'{qNum+1}. {"ABCD"[answerOptions.index(correctAnswer)]}\n')
    
    quizFile.close()
    answerFile.close()

print('Process Done!')