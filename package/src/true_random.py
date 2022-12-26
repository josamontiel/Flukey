#!/usr/bin/python3

# libs for randomization
import secrets
import string


# libraries for progressbar
from tqdm import tqdm
import time

import qr_gen_file
import click

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
    qr_gen_file.generate()


def password():
    password_len = int(input("\nLength of password: "))
    with_or_without_special_characters = input(
        "Would you like to include special characters? (Y/N): ")

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
    click.echo(click.style(f"\nHere is your Password:\n\n{yes_or_no()}\n", fg=all_colors[-3]))
    qr_gen_file.generate()


def passphrase():
    with open('/usr/share/dict/words') as f:
        passphrase_len = int(input("\nHow many words: "))
        words = [word.strip() for word in f]
        passphrase_gen = ' \n'.join(secrets.choice(words).title() for i in range(passphrase_len))
        progress_bar()
        print(f"\nHere is your Passphrase: \n\n\n{passphrase_gen}\n\n")
        qr_gen_file.generate()
