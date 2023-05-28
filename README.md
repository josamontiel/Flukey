<!--Logo will go here-->

# Flukey

###### Generate Truly Random Passcodes Right in your Terminal

**Not field tested only for demo (for now)**

## Threat model

Whether you are looking to evade a bad actor, opressive regime or just wanna secure your Facebook, a strong password is a good start. That first layer of protection will ensure that whatever you got hidden behind it will remain safe**. I truly believe that **ALL** threat models for online privacy should include some sort of password generator. generating truly secure and randomized passcodes will allow one to securely lock down whatever it is they want to protect online. Don't let people gaslight you into thinking that you need to be a whistleblower to deploy things like password generators, 2-Factor Authenticators and the like.

## Entropy

The simplest explanation I could find regarding password entropy is this quote from a cryptography forum from 2011:

###### " Information entropy is closely related to the "predictability" of the same information. When we talk about password entropy we are usually concerned with how easy it is for a password cracking software to predict a password. The more passwords the software has to try before guessing the password the larger the entropy is. "

In a nutshell, when I speak about entropy, I am speaking to the randomness of the generated passcode within the paramets set by the user. The more characters (Upper/Lower case, number and special characters) in your password, the more likely you are to fend off any bad actors. Ideally, a multiword passphrase with mixed-case letters, numbers and special characters as well as whitespace (spacebar) will ensure your data is safe.

## Why in the command line?

I elected to have this app live in the command line due to a couple of factors. But mainly because I wanted this to be lightweight and almost unnoticable. Maybe if I decide to have this go live I will name it something innocuous, but truthfully it would not need to be because this will not be a password manager so even if someone had your machine they could not get any previously derived passcodes from it.
