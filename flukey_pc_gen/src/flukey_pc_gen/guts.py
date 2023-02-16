#!/usr/bin/python3

# libs for randomization
import secrets
import string
# libraries for progressbar
from tqdm import tqdm
import time
# Library that allows for shell styling
import click

# colors for animations of the CLI when running the program
all_colors = (
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "bright_black",
    "bright_red",
    "bright_green",
    "bright_yellow",
    "bright_blue",
    "bright_magenta",
    "bright_cyan",
    "bright_white",
)


def progress_bar():
    """
    Progress bar animation
    adds a progressbar which doesn't really serve a function to the program itself, but it does look cool.
    """
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)


def pin():
    pin_len = int(input("\nLength of your new PIN: "))
    numbers = string.digits
    pin_num = ''.join(secrets.choice(numbers) for i in range(int(pin_len)))
    progress_bar()
    print(f"\nHere is your PIN:\n\n{pin_num}\n")


def password():
    """
    Password function has a couple of built-in functions:
    - choosing between special chars in PWs or not
    - determining the amount of different password iterations you would like
    """
    password_len = int(input("\nLength of password: "))
    with_or_without_special_characters = input(
        "Would you like to include special characters? (Y/N): ")
    quantity_of_passwords_to_generate = int(input("How many different passwords would you like to generate? "))
    characters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    def yes_or_no():
        password_without_spec_chars = ''.join(secrets.choice(
            characters + numbers) for i in range(password_len))
        password_with_spec_chars = ''.join(secrets.choice(
            password_without_spec_chars + special_chars) for i in range(password_len))

        if with_or_without_special_characters.lower() == "y":
            return password_with_spec_chars
        else:
            return password_without_spec_chars
    '''
    The below if statement will print off a warning to the user that the password
    they have selected is very short and increases the likelihood of being cracked
    '''
    if password_len <= 12:
        click.echo(click.style("""
            Your password is pretty weak, 
            this will increase the likelihood of your password being brute forced. 

            Consider a longer password (Ideally more than 18 characters).
                """, fg=all_colors[1], bold=True))
        to_continue = input("Would you like to continue anyway?(Y/N): ")

        if to_continue.lower() == 'y':
            yes_or_no()
        else:
            return password()

    progress_bar()

    def amount_of_passwords():
        """
         Function that instructs the program, iterations of passwords to generate depends on the number selected.
        """
        for pwd in range(quantity_of_passwords_to_generate):
            passwords = ''
            for c in range(password_len):
                passwords += yes_or_no()
            click.echo(yes_or_no())

    click.echo(click.style(f"\nTA-DA:\n\n{amount_of_passwords()}\n", fg=all_colors[-3]))



def passphrase():
    """
    This function draws words that is stored in a computers internal dictionary.
    So I imagine that the words may vary depending on the language?
    """
    with open('/usr/share/dict/words') as f:
        passphrase_len = int(input("\nHow many words: "))
        words = [word.strip() for word in f]
        passphrase_gen = ' \n'.join(secrets.choice(words).title() for i in range(passphrase_len))
        progress_bar()
        print(f"\nHere is your Passphrase: \n\n\n{passphrase_gen}\n\n")
