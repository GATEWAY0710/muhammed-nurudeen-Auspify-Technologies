import random
import string
import sys

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    """Generate a random secure password based on user preferences."""
    if length < 1:
        raise ValueError("Password length must be at least 1")
    
    character_pool = ''
    if use_letters:
        character_pool += string.ascii_letters
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("=" * 40)
    print("   PASSWORD GENERATOR")
    print("=" * 40)
    print()
    
    try:
        # Get password length
        length_input = input("Enter password length: ").strip()
        length = int(length_input)
        
        if length < 4:
            print("Warning: Passwords shorter than 4 characters may be less secure.")
        
        print("\nInclude the following? (y/n)")
        use_letters = input("Letters (a-z, A-Z): ").strip().lower() != 'n'
        use_digits = input("Numbers (0-9): ").strip().lower() != 'n'
        use_symbols = input("Symbols (!@#$...): ").strip().lower() != 'n'
        
        # Check if at least one option selected
        if not (use_letters or use_digits or use_symbols):
            print("\nError: You must select at least one character type!")
            return
        
        # Get number of passwords
        count_input = input("\nHow many passwords to generate? (default 1): ").strip()
        count = int(count_input) if count_input else 1
        
        if count < 1:
            count = 1
        
        print("\n" + "=" * 40)
        print("   GENERATED PASSWORD(S)")
        print("=" * 40)
        
        for i in range(count):
            password = generate_password(length, use_letters, use_digits, use_symbols)
            print(f"{i + 1}. {password}")
        
        print("=" * 40)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except EOFError:
        print("\n\nOperation cancelled.")
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")

if __name__ == "__main__":
    main()
