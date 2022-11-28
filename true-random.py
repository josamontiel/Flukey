##### TRUE RANDOM #####

import secrets
import string

#libraries for progressbar
from tqdm import tqdm
import time

# Progress bar animation
def progress_bar():
    for i in tqdm (range (101),
                   desc="Loading…",
		           ascii=False, ncols=75):
	    time.sleep(0.01)

# Prompt user to make selection
choose_option = int(input("\nWhat would you like to generate?\n\n (1) PIN number\n (2) Password\n (3) Passphrase\n\n"))
    
# Function for pin number
def pin_gen():
    pin_len = int(input("\nLength of your new PIN: ")) 
    numbers = string.digits
    pin_num = ''.join(secrets.choice(numbers)for i in range(int(pin_len)))
    progress_bar() 
    print(f"\nHere is your PIN: \n\n\n{pin_num}\n\n")

# Function for password
def password_gen():
        password_len = int(input("\nLength of password: "))

        lower_alpha = string.ascii_lowercase 
        upper_alpha = string.ascii_uppercase
        numbers = string.digits

        password = ''.join(secrets.choice(lower_alpha + upper_alpha + numbers)  for i in range (password_len))
        progress_bar() 
        print(f"\nHere is your Password: \n\n\n{password}\n\n")

# Function for passphrase
def passphrase_gen():
        with open('/usr/share/dict/words') as f:
                passphrase_len = int(input("\nHow many words: "))
                words = [word.strip() for word in f]
                passphrase = ' '.join(secrets.choice(words) for i in range(passphrase_len))
                progress_bar() 
                print(f"\nHere is your Passphrase: \n\n\n{passphrase}\n\n")


def gen_choices():

    if choose_option == int('1'):
        return pin_gen()
    elif choose_option == int('2'):
        return password_gen()
    elif choose_option == int('3'):
        return passphrase_gen()
    else:
        return choose_option

gen_choices()

