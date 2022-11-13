##### TRUE RANDOM #####

# Generate truly random PINs, Passwords and Passphrases 
# 
# 
# 
# 
# 
# 
# 
# #

# #TODO 
# 
#  1. Ask user what they would like to generate
#  2. Have separate functions for each selection
#  3. Run the respective selection based on the choice of the user
# 
# 
# 
# END 

import secrets
import string
# import numbers / For generating PIN numbers?

# select_input = input("What would you like to generate?\n 1. A PIN number.\n 2. A Password.\n 3.A Passphrase. \n (Select 1, 2 or 3)") 
# 
# # Asks user if they would like to generate a PIN, PW or Phrase




# pin_len = int(input("How many numbers would you like your PIN to have: ")) / PIN input
# passphrase_len = int(input("How many words would you like in your passphrase: "))


password_len = int(input("Length of password: "))

lower_alpha = string.ascii_lowercase + string.digits
upper_alpha = string.ascii_uppercase + string.digits

password_gen = ''.join(secrets.choice(lower_alpha + upper_alpha) for i in range (length))

# Generate multi word passphrase
# with open('/usr/share/dict/words') as ppdic:
#     words = [word.strip() for word in ppdic]
#     password_gen = ' '.join(secrets.choice(words)for i in range(4))


print(password_gen)