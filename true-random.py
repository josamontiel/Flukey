##### TRUE RANDOM #####

#Library for generating random/secure numbers or letters
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
    # create_text_file()

# Function for password
def password_gen():
        password_len = int(input("\nLength of password: "))

        lower_alpha = string.ascii_lowercase 
        upper_alpha = string.ascii_uppercase
        numbers = string.digits

        password = ''.join(secrets.choice(lower_alpha + upper_alpha + numbers)  for i in range (password_len))
        progress_bar() 
        print(f"\nHere is your Password: \n\n\n{password}\n\n")
        # create_text_file()

# Function for passphrase
def passphrase_gen():
        with open('/usr/share/dict/words') as f:
                passphrase_len = int(input("\nHow many words: "))
                words = [word.strip() for word in f]
                passphrase = ' '.join(secrets.choice(words) for i in range(passphrase_len))
                progress_bar() 
                print(f"\nHere is your Passphrase: \n\n\n{passphrase.title()}\n\n")
                # create_text_file()


def gen_choices():
    
    c = choose_option

    if c == int('1'):
        return pin_gen()
    elif c == int('2'):
        return password_gen()
    elif c == int('3'):
        return passphrase_gen()
    else:
        return c
    
# def make_my_file():
#     make_file = input("Would you like to copy this to a text file (Y/N): ")
#          # Function to create output file
#     def create_text_file():
#         with open("output.txt", "w") as my_file:
#             my_file.write()

#     if make_file == 'Y' or 'y':
#         return create_text_file()
#     else:
#         return choose_option
   
gen_choices()
# make_my_file()
