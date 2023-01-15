import secrets
import string
from shell_functionality import *
from qr_gen_file import *
from progressbar import progress_bar

def pin():
    """
    The functionality for the pin is pretty straightforward,
    the pin length is selected and it takes the digits method 
    from the string library to give us '0-9'.
    The secrets.choice method allows us to get a random selection
    based on the length of our pin we selected, giving us the finished product
    """
    pin_len = int(input("\nLength of your new PIN: "))
    numbers = string.digits
    pin_num = ''.join(secrets.choice(numbers) for i in range(int(pin_len)))
    progress_bar()
    print(f"\nHere is your PIN:\n\n{pin_num}\n")
    qr_code_generate()
