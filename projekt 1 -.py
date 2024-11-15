
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Riegel
email: honzikriegel@gmail.com
"""


oddelovac = 30*'='
uziv_jm = ['bob', 'ann', 'mike', 'liz']
jmeno = input('Zadej uživatelské jméno: ')
heslo = input('Zadej heslo: ')
heslo_1 = '123'
heslo_2 = 'pass123'
heslo_3 = 'password123'
heslo_4 = 'pass123'
if jmeno in uziv_jm[0]:
    if heslo == heslo_1:
        print('Welcome to the app,',jmeno,'We have 3 texts to be analyzed.')
    else:
        print('unregistered user, terminating the program..')
        quit()
elif jmeno in uziv_jm[1]:
    if heslo == heslo_2:
        print('Welcome to the app,',jmeno,'We have 3 texts to be analyzed.')
    else:
        print('unregistered user, terminating the program..')
        quit()
elif jmeno in uziv_jm[2]:
    if heslo == heslo_3:
        print('Welcome to the app,',jmeno,'We have 3 texts to be analyzed.')
    else:
        print('unregistered user, terminating the program..')
        quit()
elif jmeno in uziv_jm[3]:
    if heslo == heslo_4:
        print('Welcome to the app,',jmeno,'We have 3 texts to be analyzed.')  
    else:
        print('unregistered user, terminating the program..')
        quit()         
else:
    print('unregistered user, terminating the program..')
    quit()

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


print(oddelovac)
cislo = input('Enter a number btw. 1 and 3 to select: ')
print(oddelovac)
if cislo == '1':
    print('text 1')
elif cislo == '2':
    print('text 2')
elif cislo == '3':
    print('text 3')    
else:
    print('not in list \nterminating the program..')
    quit()   

cislo_int = int(cislo)
text_rozbor = (TEXTS[(cislo_int - 1)])

import re

def textstatistic(text_rozbor):
    
    words = text_rozbor.split()
    
    
    total_words = len(words)
    titlecase_words = list()
    for word in words:
        if word.istitle():
            titlecase_words.append(word)
    uppercase_words = list()
    for word in words:
        if word.isupper() and word.isalpha():
            uppercase_words.append(word)
    lowercase_words = list()
    for word in words:
        if word.islower():
            lowercase_words.append(word)
    num_tc = len(titlecase_words)
    num_uc = len(uppercase_words)
    num_lc = len(lowercase_words)

   
    numbers = re.findall(r'\b\d+\b', text_rozbor)
    total_numbers = len(numbers)
    sum_of_numbers = sum(int(num) for num in numbers)
    

    print('There are',total_words,' words in the selected text.')
    print('There are',num_tc,' titlecase words.')
    print('There are',num_uc,' uppercase words.')
    print('There are',num_lc,' lowercase words.')
    print('There are',total_numbers,' numeric strings.')
    print('The sum of all the numbers ',sum_of_numbers)


textstatistic(text_rozbor)
print(oddelovac)
print(f"{'LEN':<5}|{'OCCURENCES':<13}|{'NR.'}")
print(oddelovac)

from collections import Counter
words = text_rozbor.split()


lengths = [len(word) for word in words]
counter = Counter(lengths)

for length in range(1, max(counter.keys()) + 1):
    occurrences = counter.get(length, 0)
    print(f"{length:<5}|{'*' * occurrences:<13}|{occurrences}")


quit()    

