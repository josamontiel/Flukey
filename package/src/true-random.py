#!/usr/bin/python3

##### TRUE RANDOM #####

#Library for generating random/secure numbers or letters
import secrets
import string
import qrcode
import qrcode.image.svg

#libraries for progressbar
from tqdm import tqdm
import time

# Progress bar animation
def progress_bar():
    for i in tqdm (range (101),
                   desc="Loading…",
		           ascii=False, ncols=75):
	    time.sleep(0.01)
     

class QR_CODE:
    pass

# Prompt user to make selection
# choose_option = int(input("\nWhat would you like to generate?\n\n (1) PIN number\n (2) Password\n (3) Passphrase\n\n"))
    
# Function for pin number
def pin_gen():
    pin_len = int(input("\nLength of your new PIN: ")) 
    numbers = string.digits
    pin_num = ''.join(secrets.choice(numbers)for i in range(int(pin_len)))
    progress_bar() 
    print(f"\nHere is your PIN: \n\n\n{pin_num}\n\n")
    
    def qr_gen():
    
        save_to_qr = print(input("Would you like to save this PIN on a QR code? (Y/N): "))
    
        type(save_to_qr)
    
        save_to_qr = qrcode.make(f"{pin_num}")
    
        if save_to_qr == "Y" or "y":
            return save_to_qr.save("rename.png")
        else:
            return 
    qr_gen()

# Function for password
def password_gen():
        password_len = int(input("\nLength of password: "))
        with_or_without_special_characters = input("Would you like to include special characters? (Y/N): ")

        lower_alpha = string.ascii_lowercase 
        upper_alpha = string.ascii_uppercase
        numbers = string.digits
        special_chars = string.punctuation

        password_without_spec_chars = ''.join(secrets.choice(lower_alpha + upper_alpha + numbers)  for i in range (password_len))
        password_with_spec_chars = ''.join(secrets.choice(password_without_spec_chars + special_chars)  for i in range (password_len))
        
        def yes_or_no():
            if with_or_without_special_characters == "Y" or with_or_without_special_characters == "y":
                return password_with_spec_chars
            else:
                return password_without_spec_chars
            
        progress_bar() 
        print(f"\nHere is your Password: \n\n\n{yes_or_no()}\n\n")
        
        def qr_gen():
    
            save_to_qr = print(input("Would you like to save this on a QR code? (Y/N): "))
    
            type(save_to_qr)
    
            save_to_qr = qrcode.make(f"{yes_or_no()}")
    
            if save_to_qr == "Y" or "y":
                return save_to_qr.save("rename.png")
            else:
                return 
        qr_gen()

# Function for passphrase
def passphrase_gen():
        with open('/usr/share/dict/words') as f:
                passphrase_len = int(input("\nHow many words: "))
                words = [word.strip() for word in f]
                passphrase = ' \n'.join(secrets.choice(words).title() for i in range(passphrase_len))
                progress_bar() 
                print(f"\nHere is your Passphrase: \n\n\n{passphrase}\n\n")
                
        def qr_gen():
    
            save_to_qr = print(input("Would you like to save this on a QR code? (Y/N): "))
    
            type(save_to_qr)
    
            save_to_qr = qrcode.make(f"{passphrase}")
    
            if save_to_qr == "Y" or "y":
                return save_to_qr.save("rename.png")
            else:
                return 
        qr_gen()
                
    
# def gen_choices():
    
      
#     c = choose_option
    
    
#     if c == int('1'):
#         return pin_gen()
#     elif c == int('2'):
#         return password_gen()
#     elif c == int('3'):
#         return passphrase_gen()
#     else:
#         return c
# gen_choices()

class EXECUTE():
    one = int('1')
    two = int('2')
    three = int('3')

choose_option = int(input("\nWhat would you like to generate?\n\n (1) PIN number\n (2) Password\n (3) Passphrase\n\n"))

match choose_option:
    case EXECUTE.one:
        print(pin_gen())
    case EXECUTE.two:
        print(password_gen())
    case EXECUTE.three:
        print(passphrase_gen())    
