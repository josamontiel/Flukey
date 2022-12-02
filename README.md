

## :closed_lock_with_key: Truly Random password generator :closed_lock_with_key:

## Abstract:
Using Python script you can generate completely random and secure: PINs, Passwords and multi-word Passphrases of any length you choose. Using the script allows you to choose them completely at random without your intervention.

## Introduction

For years, many of use have lived the same life with respect to how we operate online: We use the same passwords for multiple accounts for months/years, eventually forgetting and having to reset it. If you are like I was, then your 'new' password was just a variation of the old one with some slight modification. Depending on the site or service you sre creating a password for, they may ask for your lock to meet certain requirements (minimum of 8 characters long, include at least 1 numbers and special character... seem familiar?) There is a good reason for this, entropy.

> Password Entropy is a measurement of difficulty or 'randomness!'

The more letters (upper and lowercase), numbers and special characters (?/!@#$%...) you add, the harder it makes it for a hacker to [brute force attack](https://en.wikipedia.org/wiki/Brute-force_attack) your account and gain access to your sensitive data. 

#### Let's take a look at some length examples and their strengths:


<img title="Entropy guide" alt="A chart detailing length and strength of passwords" src="https://external-preview.redd.it/2l9o6Gro5JI7nZATK4kY_78KSy7HkXmWxUXnoks8uhw.jpg?auto=webp&s=a676126d5be7bd3fc5534523f9a0ca81b0dcb9a5">

> Notice with just lowercase letters it would take hackers 23Mln years to hack your accounts/data when your lock is 18 characters long... 
> 
> A word of caution though, as computers and software advance, these times will shorten drastically. Notice how a lock of only 8 characters, being mixed cased and including numbers, only takes 1 hour to crack. That is scary!

As you can see in the above chart, the more characters in your lock, the harder it makes it for hackers to use hacking software to brute force your data/accounts. Even with just numbers, it would take 9 months for a hacker to crack it when the lock is at least 18 numbers long. This will only increase when you begin to add, letters and symbols. Even adding one or two symbols increases your password entropy drastically.

### PIN Generator: 
```
What would you like to generate?

 (1) PIN number
 (2) Password
 (3) Passphrase

1

Length of your new PIN: 10
Loading…: 100%|██████████████████████████| 101/101 [00:01<00:00, 84.16it/s]

Here is your PIN: 


5249438493
```

### Password generator: 

```
What would you like to generate?

 (1) PIN number
 (2) Password
 (3) Passphrase

2

Length of password: 24
Would you like to include special characters? (Y/N): Y
Loading…: 100%|██████████████████████████| 101/101 [00:01<00:00, 84.26it/s]

Here is your Password: 


yvccSV<^W3>\.-'%;_c+'{|-
```

```
What would you like to generate?

 (1) PIN number
 (2) Password
 (3) Passphrase

2

Length of password: 24
Would you like to include special characters? (Y/N): N
Loading…: 100%|██████████████████████████| 101/101 [00:01<00:00, 84.31it/s]

Here is your Password: 


t2Ak1ZrGcYIpIRidRbvwt0ak
```

### Passphrase Generator:

```
What would you like to generate?

 (1) PIN number
 (2) Password
 (3) Passphrase

3

How many words: 10
Loading…: 100%|██████████████████████████| 101/101 [00:01<00:00, 84.38it/s]

Here is your Passphrase: 


Incorporator 
Settleable 
Medicamentation 
Notidanian 
Balantidium 
Flong 
Pleasurehood 
Geochronology 
Sultam 
Onychoid
```

## :warning: **Warning:** This password generator is not field tested, please understand that if you decide to use this that you are doing so at your own risk.
