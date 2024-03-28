import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    
    combination = string.ascii_lowercase + string.digits
    mandatory_parts = ""

    if symbols:
        combination += string.punctuation
        mandatory_parts += secrets.choice(string.punctuation)

    if uppercase:
        combination += string.ascii_uppercase
        mandatory_parts += secrets.choice(string.ascii_uppercase)

    # Adjust the length for mandatory characters
    remaining_length = length - len(mandatory_parts)
    new_password = ""

    for _ in range(remaining_length):
        new_password += secrets.choice(combination)

    for char in mandatory_parts:
        insert_at = secrets.randbelow(len(new_password) + 1)
        new_password = new_password[:insert_at] + char + new_password[insert_at:]
    
    return new_password

if __name__ == "__main__":
    for i in range(1, 6):
        new_password = generate_password(length=2, symbols=True, uppercase=True)
        specs = f"U: {contains_upper(new_password)} S: {contains_symbols(new_password)}"
        
        print(f"{i} -> {new_password} ({specs})")