from random import choice

def run_game():
    word_list = ['hund', 'katze', 'maus', 'haus', 'pelikan']
    word = choice(word_list)

    user_name = input('Bitte gebe deinen Namen ein: ').strip()
    print(f'Willkommen zu Hangman, {user_name}!')

    guessed = ''
    tries = 3

    while tries > 0:
        print('Wort: ', end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
        print('\n')

        if '_' not in [char if char in guessed else '_' for char in word]:
            print('Richtig!')
            break

        while True:
            guess = input('Gebe einen Buchstaben ein: ').lower().strip()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print('Bitte gebe genau einen Buchstaben ein.')
        
        if guess in guessed:
            print(f'Den Buchstaben {guess} hast du bereits geraten.')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Das war leider falsch, du hast noch {tries} Versuche.')

    if tries == 0:
        print(f'Du hast keine Versuche mehr, du hast verloren. Das Wort war {word}.')

if __name__ == '__main__':
    run_game()
