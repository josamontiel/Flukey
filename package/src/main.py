import true_random


def main_menu():
    print("""
        Welcome to True Random!!!
-->Generate truly random PINs/Passwords/Passphrases<--

Select an option below:
-- PIN

-- Password

-- Passphrase
           """)
    selection = input("> ").lower()
    if selection == 'pin':
        return true_random.pin()
    elif selection == 'password':
        return true_random.password()
    elif selection == 'passphrase':
        return true_random.passphrase()
    else:
        print("Please make a valid selection!")


main_menu()
