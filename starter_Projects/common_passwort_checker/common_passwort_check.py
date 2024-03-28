def check_passwort(passwort:str):
    with open('password-list-top-100000.txt',encoding="utf-8") as file:   
        common_passwords: list[str] = file.read().splitlines()

        for i, common_password in enumerate(common_passwords, start=1):
            if passwort == common_password:
                print(f"{passwort}: ist das (#{i}) häufigste Passwort")
                return
        print(f"{passwort}: ist nicht in den Top 100.000 häufigsten Passwörter")


def main():
    while True:
        user_input:str = input("Gibt ein Passwort ein: ")
        if user_input == "":
            print("Bitte gib ein gültiges Passwort ein ")
        else:
            break
    check_passwort(user_input)

if __name__ == "__main__":
    main()