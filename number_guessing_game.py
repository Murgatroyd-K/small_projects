from random import randint

lower_num , higher_num = 1,10
i = 0
user_trys_limit = 3
random_num:int = randint(lower_num,higher_num)

print(f'Errate meine Zahl welche zwischen {lower_num} und {higher_num} liegt, du hast {user_trys_limit} Versuche.')

while i < user_trys_limit:
    try:
        user_guess:int = int(input(f'Versuch {i+1}: '))
    except ValueError as e:
        print('Bitte gebe eine Gültige Zahl ein')
        continue
    if user_guess > random_num:
        print('Die Zahl ist kleiner')
    elif user_guess < random_num:
        print('Die Zahl ist größer')
    elif user_guess == random_num:
        print(f'Richtig, die Zahl ist {user_guess}')
        break
    i+=1
else:
    print(f'Game Over, meine Zahl war {random_num}')