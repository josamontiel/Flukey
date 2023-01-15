import secrets
import string
from progressbar import progress_bar
from shell_functionality import *

def password():
    """
    Password function has a couple of built-in functions:
    - choosing between special chars in PWs or not
    - determining the amount of different password iterations you would like
    """
    password_len = int(input("\nLength of password: "))
    with_or_without_special_characters = input(
        "Would you like to include special characters? (Y/N): ")
    quantity_of_passwords_to_generate = int(input("How many different passwords would you like to generate? "))
    characters = string.ascii_letters
    numbers = string.digits
    special_chars = string.punctuation

    def yes_or_no():
        """
        This function allows for the selection of
        passwords with or without special characters,
        ideally one should always have special characters in their 
        passwords but they are not necessary for strong passwords,
        it just allows for better entropy with less characters 
        """
        password_without_spec_chars = ''.join(secrets.choice(
            characters + numbers) for i in range(password_len))
        password_with_spec_chars = ''.join(secrets.choice(
            password_without_spec_chars + special_chars) for i in range(password_len))

        if with_or_without_special_characters.lower() == "y":
            return password_with_spec_chars
        else:
            return password_without_spec_chars
    '''
    The below if statement will print off a warning to the user that the password
    they have selected is very short and increases the likelihood of being cracked
    '''
    if password_len <= 12:
        click.echo(click.style("""
            Your password is pretty weak, 
            this will increase the likelihood of your password being brute forced. 

            Consider a longer password (Ideally more than 18 characters).
                """, fg=all_colors[1], bold=True))
        to_continue = input("Would you like to continue anyway?(Y/N): ")

        if to_continue.lower() == 'y':
            yes_or_no()
        else:
            return password()

    progress_bar()
    
password()
