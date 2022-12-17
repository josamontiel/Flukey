
#!/bin/bash
<<com
Shell script to run program from Terminal.

Aim is to have this script execute the generator from the terminal, without the need of entering extra commands.
com

<<instructions
    Have args for each functions:
        - password
        - pin
        - passphrase
    Example: run <arg: password> run password.py

    separate true random into 3 files for separation of actions 
instructions

<<help
convert documentation into a help feature for the command line and allow for execution in the terminal
help

###################################################################
pin=$(filename that corresponds with file)
if [[arg==pin]]
./pin.py
else if [[arg==password]]
./password.py
else if [[arg==passphrase]]
./passphrase.py
fi
