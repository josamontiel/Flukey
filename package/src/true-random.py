#!/usr/bin/python3


# import typing
# import os
# import sys
# import pydoc

# libs for randomization
import secrets
import string
# qr code libraries
import qrcode
import qrcode.image.svg
# libraries for progressbar
from tqdm import tqdm
import time


def progress_bar():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)


class qr_Code:
    def generate(code_type):
        save_to_qr = input("Would you like to save this on a QR code? (Y/N): ")
        type(save_to_qr)
        save_to_qr = qrcode.make(f"{code_type}")

        if save_to_qr == "Y" or "y":
            return save_to_qr.save("newfile.png")
        else:
            pass


def pin_generate():
    pin_len = int(input("\nLength of your new PIN: "))
    numbers = string.digits
    pin_num = ''.join(secrets.choice(numbers) for i in range(int(pin_len)))
    progress_bar()
    print(f"\nHere is your PIN: \n\n\n{pin_num}\n\n")
    qr_Code.generate(pin_num)


def password_generate():
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
    qr_Code.generate(yes_or_no())


def passphrase_generate():
    with open('/usr/share/dict/words') as f:
        passphrase_len = int(input("\nHow many words: "))
        words = [word.strip() for word in f]
        passphrase = ' \n'.join(secrets.choice(words).title()
                                for i in range(passphrase_len))
        progress_bar()
        print(f"\nHere is your Passphrase: \n\n\n{passphrase}\n\n")
        qr_Code.generate(passphrase)


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
        return pin_generate()
    elif selection == 'password':
        return password_generate()
    elif selection == 'passphrase':
        return passphrase_generate()
    else:
        print("Please make a valid selection!")


main_menu()
