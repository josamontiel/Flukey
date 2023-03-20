#!/usr/bin/python3

# The MIT License (MIT)

# Copyright (c) 2023 Joseph A. M. 

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#################################################################################
# FLUKEY LITE

# The purpose of having a lite version of the app is purely for the super paranoid. 
# Having a text user interface is great, it's so much better than having to depend 
# on a GUI and has far less bloat. Allowing for almost identical functionality with 
# this lighter version this will have less dependencies which means far more portable 
# as it only uses standard libraries. 
# 
# Enjoy!
#################################################################################

import secrets
import string
import time
import os
import argparse
import sys
import subprocess

def clear_screen(time:int):
    time = time.sleep(5)
    return os.system('clear')

def PIN():
    """
    The generation of any pins longer than 
    a couple of digits is not really used in
    daily life for most, but it costs nothing
    to provide that functionality
    """
    NUMBERS = string.digits
    LENGTH=int(input("\nLENGTH OF DESIRED PIN: "))
    PIN_NUM = ''.join(secrets.choice(NUMBERS) for _ in range(int(LENGTH)))
    print(f"\n\nHERE IS YOUR NEW PIN:\n\n{PIN_NUM}")
    clear_screen(time)
    
def PASSWORD():
    """
    The ability to generate passwords is really
    the bulk of this app, passwords are used far
    more frequently than PINs or PASSPHRASES.
    """
    CHARACTERS=string.ascii_letters+string.digits+string.punctuation
    LENGTH=int(input("enter desired password length: "))
    PASSWORD_GEN=''.join(secrets.choice(CHARACTERS) for _ in range(int(LENGTH)))
    print(f"\n\nHERE IS YOUR NEW PASSWORD:\n\n{PASSWORD_GEN}")
    clear_screen(time)
    
def PASSPHRASE():
    """
    Generating a multi-word passphrase does not
    have many uses, I suppose if you were very paranoid
    you could generate all of your passwords using multi-word
    passphrases, which, including white spaces would be very safe.
    But having only words is not enough to stop brute force attacks, 
    especially since machines are getting stronger and stronger.
    """
    with open('wordlist.txt') as f:
        LENGTH=int(input("HOW MANY WORDS WOULD YOU LIKE TO GENERATE: "))
        WORDS = [word.strip() for word in f]
        PASSPHRASE_GEN = '\n'.join(secrets.choice(WORDS).title() for _ in range(LENGTH))
        print(f"\nHere is your Passphrase: \n\n\n{PASSPHRASE_GEN}\n\n")
    clear_screen(time)
    


PIN()
# PASSWORD()
# PASSPHRASE()

    
