"""
Exercise No. 255

Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different
signal durations, called dots and dashes.

All characters are represented by a series of signals of several elements - short (dots) and long (dashes). The duration
of the dash is at least three times the duration of the dot.

We also need to add spaces in encrypted messages. The space between the elements of the sign should be one dot. Space
between individual characters - three dots and space between groups of characters (words) - seven dots.

We only use capital letters of the alphabet.

Dictionary mapping characters to Morse code:

    MORSE_CODE = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        '&': '.-...',
        '@': '.--.-.',
        ':': '---...',
        ',': '--..--',
        '.': '.-.-.-',
        ''': '.----.',
        ''': '.-..-.',
        '?': '..--..',
        '/': '-..-.',
        '=': '-...-',
        '+': '.-.-.',
        '-': '-....-',
        '(': '-.--.',
        ')': '-.--.-',
        ' ': '.......'
    }

The letters 'a' and 'A' have the same code '.-'.

Example:

    [message]: 'PYTHON 3.9'
    [output]: '.--. -.-- - .... --- -.'

Example:

    [message]: 'HOLD YOUR POSITIONS!'
    [morse code]: '.... --- .-.. -.. / -.-- --- ..- .-. / .--. --- ... .. - .. --- -. ... -.-.--'

A function called encrypt() has been implemented that encrypts message into Morse code:

    def encrypt(message):
        return ' '.join([MORSE_CODE[char.upper()] if char != ' ' else '/' for char in message])

Implement a function called decrypt() that decrypts the message. Return the message in capital letters.

Example:

    [IN]: decrypt('.--. -.-- - .... --- -. / ...-- .-.-.- ----. ')
    [OUT]: 'PYTHON 3.9'

Example:

    [IN]: decrypt('.... --- .-.. -.. / -.-- --- ..- .-. / .--. --- ... .. - .. --- -. ... -.-.--')
    [OUT]: 'HOLD YOUR POSITIONS!'

You just need to implement the decrypt() function. The tests run several test cases to validate the solution.
"""
# Solution I

MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    ' ': '.......'
}


def encrypt(message):
    return ' '.join(
        [
            MORSE_CODE[char.upper()] if char != ' ' else '/'
            for char in message
        ]
    )


def decrypt(message):
    result = ''
    for word in message.split(' / '):
        for char in word.split(' '):
            for key, value in MORSE_CODE.items():
                if value == char:
                    result += key
        result += ' '
    return result.strip().upper()


print(decrypt('.--. -.-- - .... --- -. / ...-- .-.-.- ----. '))


# Solution II
MORSE_CODE_REVERSED = {val: key for key, val in MORSE_CODE.items()}


def encrypt(message):
    return ' '.join(
        [
            MORSE_CODE[char.upper()] if char != ' ' else '/'
            for char in message
        ]
    )


def decrypt(message):
    decipher = ''
    for char in message.split():
        if char != '/':
            decipher += MORSE_CODE_REVERSED[char]
        else:
            decipher += ' '
    return decipher


print(decrypt('.--. -.-- - .... --- -. / ...-- .-.-.- ----. '))


# Solution III
def decrypt(message):
    return ''.join(
        [
            MORSE_CODE_REVERSED[char] if char != '/' else ' '
            for char in message.split()
        ]
    )


print(decrypt('.--. -.-- - .... --- -. / ...-- .-.-.- ----. '))
