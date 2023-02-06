str = input()
happy = str.count(':-)')
sad = str.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')