import pyinputplus as pyip
import random
import time
import sys

numOfQuestions = int(sys.argv[1])
correctAnswer = 0

for qNum in range(numOfQuestions):
    num1 = random.randint(2, 9)
    num2 = random.randint(1, 9)
    prompt = f'No.{qNum+1}: {num1} x {num2} = '

    try:
        pyip.inputStr(prompt=prompt, allowRegexes=[f'^{num1*num2}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=3, limit=2)
    except:
        print('Chance missed')
    else:
        print('Correct!')
        correctAnswer += 1
    
    time.sleep(0.5)

print(f'Score: {correctAnswer} / {numOfQuestions}')