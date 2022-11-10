# Secrets Library generates truly random and secure numbers/strings
# the 'Random' library DOES NOT do the same thing. Random only generates pseudo random

import secrets
import string

length = int(input("Length of password: "))

lower_alpha = string.ascii_lowercase + string.digits
upper_alpha = string.ascii_uppercase + string.digits

password_gen = ''.join(secrets.choice(lower_alpha + upper_alpha) for i in range (length))

print(password_gen)


# TODO
# 1. Ask user if they would like to generate P/W or PIN.
# Ask user if they would like to generate a new password.