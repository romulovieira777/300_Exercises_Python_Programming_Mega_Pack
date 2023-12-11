"""
Exercise No. 251

In cryptography, a Caesar cipher, is one of the simplest and most widely known encryption techniques. It is a type of
substitution cipher in which each letter in the string is replaced by a letter some fixed number of positions down the
alphabet.

An example of the encryption. Consider only capital letters in English (let's just call it alphabet):

    ABCDEFGHIJKLMNOPQRSTUVWXYZ

Shifting the above alphabet by a certain number (key = 2) gives us the cipher:

    CDEFGHIJKLMNOPQRSTUVWXYZAB

Let's put in together:

    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    CDEFGHIJKLMNOPQRSTUVWXYZAB

Note that for the last letters of the alphabet (Y, Z) the initial letters are matched.

Having an alphabet and a cipher, we can start encrypting. Consider the message below:

    'ATTACK AT DAWN!'

Using the Caesar cipher with an offset of 2 (key = 2) we get:

    'CVVCEM CV FCYP!'

Functions named: generate_cipher() and encrypt() have been implemented. The first generates a cipher, the second
encrypts the message.

You are one of Caesar's commanders and you need to decode a message that is critical to the success of your mission.
Implement a function called decrypt() that takes three arguments:

    - alphabet - the alphabet we want use for encryption
    - message - the message we want to encrypt
    - key - key, offset

and decrypted the message.

In the implementation, you can use the encrypt() function.

Example:

    [IN]: import string
    [IN]: decrypt(string.ascii_uppercase, 'RAVJQP', 2)
    [OUT]: PYTHON

Example:

    [IN]: import string
    [IN]: decrypt(string.ascii_uppercase, 'CVVCEM CV FCYP!', 2)
    [OUT]: ATTACK AT DAWN!

Example:

    [IN]: import string
    [IN]: decrypt(string.ascii_uppercase, 'FGBC GUR NGGNPX!', 13)
    [OUT]: STOP THE ATTACK!

You just need to implement the decrypt() function. The tests run several test cases to validate the solution.
"""
# Solution I
import string


def generate_cipher(alphabet, key):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher


def encrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += cipher[alphabet.index(letter)]
    return result


def decrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += alphabet[cipher.index(letter)]
    return result


print(decrypt(string.ascii_uppercase, 'RAVJQP', 2))
print(decrypt(string.ascii_uppercase, 'CVVCEM CV FCYP!', 2))
print(decrypt(string.ascii_uppercase, 'FGBC GUR NGGNPX!', 13))


# Solution II
import string


def generate_cipher(alphabet, key):
    cipher = ''
    for letter in alphabet:
        new_idx = (alphabet.index(letter) + key) % len(alphabet)
        cipher += alphabet[new_idx]
    return cipher


def encrypt(alphabet, message, key):
    cipher = generate_cipher(alphabet, key)
    result = ''
    for letter in message:
        if letter not in alphabet:
            result += letter
        else:
            result += cipher[alphabet.index(letter)]
    return result


def decrypt(alphabet, message, key):
    key = (-1) * key
    return encrypt(alphabet, message, key)


print(decrypt(string.ascii_uppercase, 'RAVJQP', 2))
print(decrypt(string.ascii_uppercase, 'CVVCEM CV FCYP!', 2))
print(decrypt(string.ascii_uppercase, 'FGBC GUR NGGNPX!', 13))
