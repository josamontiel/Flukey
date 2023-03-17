#!/usr/bin/python3

# The MIT License (MIT)

# Copyright (c) 2023 Joseph A. M. 

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#################################################################################
# FLUKEY LITE

# The purpose of having a lite version of the app is purely for the super paranoid. 
# Having a text user interface is great, it's so much better than having to depend 
# on a GUI and has far less bloat. Allowing for almost identical functionality with 
# this lighter version this will have less dependencies which means far more portable 
# as it only uses standard libraries. 
# 
# Enjoy!
#################################################################################

import secrets
import string


def PIN():
    """
    The generation of any pins longer than 
    a couple of digits is not really used in
    daily life for most, but it costs nothing
    to provide that functionality
    """
    NUMBERS=string.digits
    LENGTH=int(input("\nLENGTH OF DESIRED PIN: "))
    PIN_NUM=''.join(secrets.choice(NUMBERS) for _ in range(int(LENGTH)))
    print(f"\n\nHERE IS YOUR NEW PIN:\n\n{PIN_NUM}")
    
def PASSWORD():
    pass
def PASSPHRASE():
    pass

PIN()

# def pin():
#     pin_len = int(input("\nLength of your new PIN: "))
#     numbers = string.digits
#     pin_num = ''.join(secrets.choice(numbers) for i in range(int(pin_len)))
#     print(f"\nHere is your PIN:\n\n{pin_num}\n")


# def password():
#     """
#     Password function has a couple of built-in functions:
#     - choosing between special chars in PWs or not
#     - determining the amount of different password iterations you would like
#     """
#     password_len = int(input("\nLength of password: "))
#     with_or_without_special_characters = input(
#         "Would you like to include special characters? (Y/N): ")

#     characters = string.ascii_letters
#     numbers = string.digits
#     special_chars = string.punctuation

#     def yes_or_no():
#         password_without_spec_chars = ''.join(secrets.choice(
#             characters + numbers) for i in range(password_len))
#         password_with_spec_chars = ''.join(secrets.choice(
#             password_without_spec_chars + special_chars) for i in range(password_len))

#         if with_or_without_special_characters.lower() == "y":
#             return password_with_spec_chars
#         else:
#             return password_without_spec_chars
#     '''
#     The below if statement will print off a warning to the user that the password
#     they have selected is very short and increases the likelihood of being cracked
#     '''
#     if password_len <= 12:
#         print("""
#             Your password is pretty weak, 
#             this will increase the likelihood of your password being brute forced. 

#             Consider a longer password (Ideally more than 18 characters).
#                 """)
#         to_continue = input("Would you like to continue anyway?(Y/N): ")

#         if to_continue.lower() == 'y':
#             yes_or_no()
#         else:
#             return password()

#     print(f"\nTA-DA:\n\n{amount_of_passwords()}\n")



# def passphrase():
#     """
#     This function draws words that is stored in a computers internal dictionary.
#     So I imagine that the words may vary depending on the language?
#     """
#     with open('/usr/share/dict/words') as f:
#         passphrase_len = int(input("\nHow many words: "))
#         words = [word.strip() for word in f]
#         passphrase_gen = '\n'.join(secrets.choice(words).title() for i in 
# range(passphrase_len))
#         print(f"\nHere is your Passphrase: \n\n\n{passphrase_gen}\n\n")
