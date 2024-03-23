from random import randint

def roll_dice(amount:int = 1) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls:list[int] = []

    for i in range(amount):
        random_roll:int = randint(1,6)
        rolls.append(random_roll)
    
    return rolls

def main():
    print("Willkommen beim Würfel Simulator gibt die Anzahl an gewünschten Würfel Werten ein oder beende das Programm mit den befehl exit")
    while True:
        try:
            user_input:str = input(f'Wie viele Würfel würfel möchtest du ? \n')
            if user_input.lower() == 'exit':
                print('Danke fürs Spielen')
                break
            rolls = roll_dice(int(user_input))
            print(*rolls,sep=', ')
            print(f'Summe: {sum(rolls)}')
        except ValueError:
            print('(Bitte gib eine Gütige Zahl ein)')

if __name__ == '__main__':
    main()
