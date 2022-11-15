##### TRUE RANDOM #####

# Generate truly random PINs, Passwords and Passphrases 

# HOW IT WORKS: 
# 
#  You will be prompted to select between a PIN, Password or Passphrase
#  Upon selection you will be asked for the length of your choice
#  
# The CLI will spit out a random PIN/Password or Passphrase
# 
# END #

#Library for generating random/secure numbers or letters
import secrets
import string

#libraries for progressbar
from tqdm import tqdm
import time

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
       print("\nHere is your PIN: \n\n\n" + pin_num + "\n\n")

# Function for password
def password_gen():
        password_len = int(input("\nLength of password: "))

        lower_alpha = string.ascii_lowercase + string.digits
        upper_alpha = string.ascii_uppercase + string.digits
    
        password = ''.join(secrets.choice(lower_alpha + upper_alpha) for i in range (password_len))
        progress_bar() 
        print("\nHere is your Password: \n\n\n" + password + "\n\n")

# Function for passphrase
def passphrase_gen():
        with open('/usr/share/dict/words') as f:
                passphrase_len = int(input("\nHow many words: "))
                words = [word.strip() for word in f]
                passphrase = ' '.join(secrets.choice(words) for i in range(passphrase_len))
                progress_bar() 
                print("\nHere is your Passphrase: \n\n\n" + passphrase + "\n\n")


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
