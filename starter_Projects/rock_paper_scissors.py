from random import choice
import sys

class RPS:
    def __init__(self) -> None:
        print("Wilkommen bei Stein, Schere, Papier")
        self.moves = {"stein": "Stein", "papier": "Papier", "schere": "Schere"}
        self.valid_moves = list(self.moves.keys())
        self.player_score = 0
        self.ai_score = 0

    def play_game(self):
        user_move = input("Stein, Papier oder Schere? >> ").lower()

        if user_move == "exit":
            print("Danke fürs Spielen")
            self.display_final_scores()
            sys.exit()
        
        if user_move not in self.valid_moves:
            print('Ungültige Auswahl')
            return self.play_game()

        ai_move = choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        self.display_current_scores()

    def display_moves(self, user_move: str, ai_move: str):
        print("----")
        print(f"Du hast {self.moves[user_move]} gewählt")
        print(f"AI hat {self.moves[ai_move]} gewählt")
        print("----")

    def check_move(self, user_move: str, ai_move: str):
        win_conditions = {'stein': 'schere', 'papier': 'stein', 'schere': 'papier'}
        if user_move == ai_move:
            print("Unentschieden")
        elif win_conditions[user_move] == ai_move:
            print("Du hast Gewonnen")
            self.player_score += 1
        else:
            print("Du hast Verloren")
            self.ai_score += 1

    def display_current_scores(self):
        print(f"Aktueller Stand - Spieler: {self.player_score}, AI: {self.ai_score}")

    def display_final_scores(self):
        print(f"Endstand - Spieler: {self.player_score}, AI: {self.ai_score}. Danke fürs Spielen!")

if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()
