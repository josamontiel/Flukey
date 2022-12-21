from true_random import *

if __name__ == '__main__':
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
        return pin()
    elif selection == 'password':
        return password()
    elif selection == 'passphrase':
        return passphrase()
    else:
        print("Please make a valid selection!")


main_menu()
