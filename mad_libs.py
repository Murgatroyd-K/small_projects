def get_input(word_type:str,word_selection:list[str])-> str:
    while True:
        input_user = input(f'Bitte gebe ein {word_type} aus der Liste {word_selection} ein: ') 
        if input_user in word_selection:
            return input_user
        print("Bitte nehme ein Wort aus der Liste")

verb_list:list[str] = ["programmieren","analysieren","optimieren","debuggen"]
noun_list:list[str] = ["Codezeile","Datenbank","Funktion","Schnittstelle"]

verb_0:str = get_input('Verb',verb_list)
verb_1:str = get_input('Verb',verb_list)

noun_0:str = get_input('Substantiv',noun_list)
noun_1:str = get_input('Substantiv',noun_list)

stroy:str = f"""
Ein Programmierer sagt zum anderen: Ich habe gestern Abend versucht, meinem Programm das {verb_0} der {noun_0}, aber es wollte einfach nicht funktionieren.

Der andere schaut auf und antwortet: Interessant, ich habe mein Programm trainiert, um eine {noun_1} zu {verb_1}, und es hat angefangen, eigene Codezeilen zu schreiben!

Der erste nickt anerkennend und meint: Nun, zumindest tut eines unserer Programme, was es soll. Mein Programm hat versucht, eine Kaffeemaschine zu starten und hat stattdessen das Internet gelöscht.
""" 
print(stroy)