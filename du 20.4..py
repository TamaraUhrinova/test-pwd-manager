import secrets
import string
import json
from os import path

DATA_FILENAME = 'data.txt'

PASSWORD = [
]


if path.exists(DATA_FILENAME):
    try:
        with open(DATA_FILENAME, 'r') as infile:
            PASSWORD = json.load(infile)
    except:
        PASSWORD = []

def generate_password(length, **kwargs):
    unknown = ''
    tr = ''
    for (k, v) in kwargs.items():
        if k == 'lowercase':
            if v:
                unknown += string.ascii_lowercase
                tr = ""
            else:
                tr += string.ascii_lowercase
        elif k == 'digit':
            if v:
                unknown += string.digits
                tr = ""
            else:
                if unknown == "":
                    tr += string.digits
                
        elif k == 'uppercase':
            if v:
                unknown += string.ascii_uppercase
                tr = ""
        elif k == 'punctuation':
            if v:
                unknown += string.punctuation
                tr = ""

    unknown += tr
    password = ''    
    for i in range(length):
        password += secrets.choice(unknown)
    return password


def add():
    web = input('Zadaj web adresu ')
    username = input('Zadaj užívateľské meno ')
    password = input('Zadaj heslo (ak prázdne vygeneruje sa nové) ')

    if password == '':
        password = generate_password(16, lowercase=False, digit=False, uppercase=False, punctuation=False)

    a=input("Prajete si uložiť zmeny? (ano/nie)")
    if a == "ano":
        PASSWORD.append({
            'web': web,
            'username': username,
            'password': password
        })

def dele():
    w = input('Zadajte web adresu, ktorú chcete vymazať:')
    for i in range(len(PASSWORD)):
        if PASSWORD[i].get("web") == w:
            a = input("Prajete si uložiť zmeny? (ano/nie)")
            if a == "ano":
                PASSWORD.pop(i)
                break
            else:
                break
    else:
        print("Zle zadaná web adresa.")
        
def print_menu():
    print('ADD - Zadávanie nového vstupu')
    print('DEL - Mazanie položky')
    print('VIEW - Zobrazenie položky')
    print('EXIT - Ukončenie programu')

print('Best password manager')

while True:
    print_menu()
    cmd = input('Zadaj príkaz ')
    if cmd == 'ADD':
        add()
    elif cmd == 'DEL':
        dele()
    elif cmd == 'VIEW':
        pass
    elif cmd == 'EXIT':
        break
    else:
        print('Nesprávny príkaz.')

with open('data.txt', 'w') as outfile:
    json.dump(PASSWORD, outfile)

print(PASSWORD)
