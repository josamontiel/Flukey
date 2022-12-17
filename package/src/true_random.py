#!/usr/bin/python3

# import pydoc

# libs for randomization
import secrets
import string


# libraries for progressbar
from tqdm import tqdm
import time

import qr_gen_file


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
    print(f"\nHere is your PIN: \n\n\n{pin_num}\n\n")
    qr_gen_file.qr_code_generate()


def password():
    password_len = int(input("\nLength of password: "))
    with_or_without_special_characters = input(
        "Would you like to include special characters? (Y/N): ")

    lower_alpha = string.ascii_lowercase
    upper_alpha = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    password_without_spec_chars = ''.join(secrets.choice(
        lower_alpha + upper_alpha + numbers) for i in range(password_len))
    password_with_spec_chars = ''.join(secrets.choice(
        password_without_spec_chars + special_chars) for i in range(password_len))

    def yes_or_no():
        if with_or_without_special_characters == "Y" or with_or_without_special_characters == "y":
            return password_with_spec_chars
        else:
            return password_without_spec_chars

    progress_bar()
    print(f"\nHere is your Password: \n\n\n{yes_or_no()}\n\n")
    qr_gen_file.qr_code_generate()


def passphrase():
    with open('/usr/share/dict/words') as f:
        passphrase_len = int(input("\nHow many words: "))
        words = [word.strip() for word in f]
        passphrase = ' \n'.join(secrets.choice(words).title()
                                for i in range(passphrase_len))
        progress_bar()
        print(f"\nHere is your Passphrase: \n\n\n{passphrase}\n\n")
        qr_gen_file.qr_code_generate()
