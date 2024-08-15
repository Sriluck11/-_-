import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    char_set = ''
    if use_letters:
        char_set += string.ascii_letters
    if use_numbers:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    if not char_set:
        raise ValueError("At least one character type must be selected.")
    
    return ''.join(random.choice(char_set) for _ in range(length))

def get_user_input():
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("=====================================\nInclude letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"=====================================\nGenerated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

get_user_input()
