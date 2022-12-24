from true_random import *


def main_menu():

    click.echo(click.style("""
    TRUE RANDOM: PASSCODE GENERATOR
    """, blink=True, bold=True, fg=all_colors[5]))
    click.echo(click.style("""
-->Generate truly random PINs/Passwords/Passphrases<--

Select an option below:
-- PIN

-- Password

-- Passphrase
           """, fg=all_colors[2]))

    selection = input("> ").lower()
    if selection == 'pin':
        return pin()
    elif selection == 'password':
        return password()
    elif selection == 'passphrase':
        return passphrase()
    else:
        print("!!!!PLEASE MAKE A VALID SELECTION!!!!")
        time.sleep(2)
        return main_menu()


main_menu()
