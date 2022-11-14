##### TRUE RANDOM #####

# Generate truly random PINs, Passwords and Passphrases 

# HOW IT WORKS: 
# 
#  You will be prompted to select between a PIN, Password or Passphrase
#  Upon selection you will be asked for the length of your choice
#  
# The CLI will spit out a random PIN/Password oor Passphrase
# 
# END #

#Library for generating random/secure numbers or letters
import secrets
import string

# Prompt user to make selection
def choose_option():
        return int(input("What would you like to generate?\n 1. A PIN number.\n 2. A Password.\n 3. A Passphrase. \n")) 
    
# Function for pin number
def pin_gen():
       pin_len = int(input("Length of your new PIN: ")) 
       numbers = string.digits
       pin_num = ''.join(secrets.choice(numbers)for i in range(int(pin_len))) 
       print(pin_num)

# Function for password
def password_gen():
        password_len = int(input("Length of password: "))

        lower_alpha = string.ascii_lowercase + string.digits
        upper_alpha = string.ascii_uppercase + string.digits
    
        password = ''.join(secrets.choice(lower_alpha + upper_alpha) for i in range (password_len))
        print(password)

# Function for passphrase
def passphrase_gen():
        with open('/usr/share/dict/words') as f:
                passphrase_len = int(input("How many words: "))
                words = [word.strip() for word in f]
                passphrase = ' '.join(secrets.choice(words) for i in range(passphrase_len))
                print(passphrase)


def gen_choices():
        if choose_option() == int('1'):
                return pin_gen()
        elif choose_option() == int('2'):
                return password_gen()
        else: 
                return passphrase_gen()


gen_choices()
