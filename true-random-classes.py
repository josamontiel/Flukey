# Py file for classes of true-random
import secrets
import string

# TODO #
# Create classes for each function of the generator
#
# PIN
# P/W
# P/P
# Gen()
# #

class Pin:
    def pin_gen():
        length = int(input("\nLength of your new pin: \n"))
        numbers = string.digits
        pin_num = ''.join(secrets.choice(numbers) for i in range(length))
        print("\nHere is your pin: \n\n" + pin_num)

# Pin.pin_gen()

class Password:
    def password_gen():
        length = int(input("\nLength of password: "))

        lower_alpha = string.ascii_lowercase + string.digits 
        upper_alpha = string.ascii_uppercase + string.digits
    
        pw = ''.join(secrets.choice(lower_alpha + upper_alpha) for i in range (length))
        print("\nHere is your Password: \n\n\n" + pw + "\n\n")

# Password.password_gen()

class PassPhrase:
    def passphrase_gen():
        with open('/usr/share/dict/words') as f:
                length = int(input("\nHow many words: "))
                words = [word.strip() for word in f]
                phrase = ' '.join(secrets.choice(words) for i in range(length))
                print("\nHere is your Passphrase: \n\n\n" + phrase + "\n\n")

# PassPhrase.passphrase_gen()

