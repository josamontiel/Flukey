import secrets
from qr_gen_file import *
from progressbar import *
from shell_functionality import *


def passphrase():
    

    """
    This function draws words that are stored in a machines internal dictionary.
    So I imagine that the words may vary depending on the language?
    """
    """
    Filepath to the dictionary is opened,
    the user is then asked how many word they would like their
    passphrase to be, following that, they are then 
    presented with the final output of their selection.
    """
    with open('/usr/share/dict/words') as f:
        passphrase_len = int(input("\nHow many words: "))
        words = [word.strip() for word in f]
        passphrase_gen = ' \n'.join(secrets.choice(words).title() for i in range(passphrase_len))
        progress_bar()
        print(f"\nHere is your Passphrase: \n\n\n{passphrase_gen}\n\n")
        qr_code_generate()
        
# passphrase()
