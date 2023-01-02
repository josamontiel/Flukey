import secrets
import string
from shell_functionality import *
from qr_gen_file import *
from progressbar import progress_bar

def pin():
    pin_len = int(input("\nLength of your new PIN: "))
    numbers = string.digits
    pin_num = ''.join(secrets.choice(numbers) for i in range(int(pin_len)))
    progress_bar()
    print(f"\nHere is your PIN:\n\n{pin_num}\n")
    qr_code_generate()