# A dumb game to distract you
# 7-9-22

import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep an idiot busy for hours?\n"

    response = pyip.inputYesNo(prompt)

    if response == 'no':
        print("Thank you have a nice day")
        break
        


