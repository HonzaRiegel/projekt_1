"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Riegel
email: honzikriegel@gmail.com
"""

import re

oddelovac = 30*'='
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

def overeni_uzivatele():
    
    uzivatele = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
    jmeno = input('Enter username: ')
    heslo = input('Enter password: ')
    if jmeno in uzivatele and uzivatele[jmeno] == heslo:
        print(f'Welcome to the app,{jmeno.title()}\nWe have {len(TEXTS)} to be analyzed.')

    else:
        print('unregistered user, terminating the program..')
        quit()

def vyber_textu():
    cislo = input(f'{oddelovac}\nEnter a number btw. 1 and 3 to select: ')
    print(f'\n{oddelovac}')
    if cislo.isnumeric() and int(cislo) < len(TEXTS)+1:
        print(f'text {cislo}')  
    else:
        print(f'not in list \nterminating the program..')
        quit()
    text_rozbor = TEXTS[(int(cislo) - 1)]
    return text_rozbor

def statistika():
    text_rozbor  = vyber_textu() 
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
        if word.islower() and word.isalpha():
            lowercase_words.append(word)

    num_tc = len(titlecase_words)
    num_uc = len(uppercase_words)
    num_lc = len(lowercase_words)

   
    numbers = re.findall(r'\b\d+\b', text_rozbor)
    total_numbers = len(numbers)
    sum_of_numbers = sum(int(num) for num in numbers)
    
    print(oddelovac)
    print(f'There are {total_words} words in the selected text.')
    print(f'There are {num_tc} titlecase words.')
    print(f'There are {num_uc} uppercase words.')
    print(f'There are {num_lc} lowercase words.')
    print(f'There are {total_numbers} numeric strings.')
    print(f'The sum of all the numbers is {sum_of_numbers}')

    return text_rozbor

def tvorba_grafu(): 
   
    
    text_rozbor = statistika() 
    words = text_rozbor.split()
    
    lengths = []
    
    for word in words:
        
        word_a = word.replace(",","").replace(".","")
        word_l = len(word_a)    
        lengths.append(word_l) 

    cetnosti = {}
    for cislo in lengths:
        if cislo in cetnosti:
            cetnosti[cislo] += 1
        else:
            cetnosti[cislo] = 1
    sort_sl  ={key: cetnosti[key] for key in sorted(cetnosti)} 
       
    
    print(f"{oddelovac}\n{'LEN':<5}|{'OCCURENCES':<13}|{'NR.'}\n{oddelovac}")
    for key, value in sort_sl.items(): 
        print(f"{key:<5}|{'*'* value:<13}|{value}")        

overeni_uzivatele()
tvorba_grafu()

          

                        

