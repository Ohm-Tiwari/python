# Takes clipboard and extracts any email or phone number in text
# 7-6-2022

import re
from tabnanny import verbose
import pyperclip


#Phone number regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})         #Fist 3 digits
    (\s|-|\.)
    (\d{4})         #Last 4 digits
    (\s*(exxt|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

#Email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #Username
    @                           
    [a-zA-Z0-9.-]+          #Domain name
    (\.[a-zA-Z]{2,4})       #dot-something
)''', re.VERBOSE)

#Finds matches in clipboard

text = str(pyperclip.paste())

matches=[]
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Puts results in clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print("No emails or phone numbers found.")