"""
Exercise No. 253

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

Implement a solution to this problem using the object-oriented programming (OOP) paradigm.

The CaesarCipher class is given:

    class CaesarCipher:
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (self.alphabet.index(letter) + self.key) % len(
                self.alphabet
            )
            result += self.alphabet[new_idx]
        return result

Follow the next steps in this exercise:

    1. Implement an encrypt() method that encrypts the message (message argument)
    2. Implement a decrypt() method that decrypts the message (message argument)

You just need to implement these methods. The tests run several test cases to validate the solution.
"""
# Solution I


class CaesarCipher:
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (self.alphabet.index(letter) + self.key) % len(
                self.alphabet
            )
            result += self.alphabet[new_idx]
        return result

    def encrypt(self, message):
        encrypted_message = ''
        for letter in message:
            if letter in self.alphabet:
                encrypted_message += self.cipher[self.alphabet.index(letter)]
            else:
                encrypted_message += letter
        return encrypted_message

    def decrypt(self, message):
        decrypted_message = ''
        for letter in message:
            if letter in self.alphabet:
                decrypted_message += self.alphabet[self.cipher.index(letter)]
            else:
                decrypted_message += letter
        return decrypted_message


cipher = CaesarCipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)
print(cipher)
print(cipher.encrypt('PYTHON'))
print(cipher.decrypt('RAVJQP'))


# Solution II
class CaesarCipher:
    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (self.alphabet.index(letter) + self.key) % len(
                self.alphabet
            )
            result += self.alphabet[new_idx]
        return result

    def encrypt(self, message):
        result = ''
        for letter in message:
            if letter not in self.alphabet:
                result += letter
            else:
                result += self.cipher[self.alphabet.index(letter)]
        return result

    def decrypt(self, message):
        result = ''
        for letter in message:
            if letter not in self.alphabet:
                result += letter
            else:
                result += self.alphabet[self.cipher.index(letter)]
        return result


cipher = CaesarCipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)
print(cipher)
print(cipher.encrypt('PYTHON'))
print(cipher.decrypt('RAVJQP'))
