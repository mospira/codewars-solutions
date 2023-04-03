# 5 kyu

# TAGS {CIPHERS} {FUNDAMENTALS}

# DESCRIPTION:
# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating

import string

def rot13(message):
    result = []
    lowers, uppers = list(string.ascii_lowercase),list(string.ascii_uppercase)
    result = [lowers[(lowers.index(letter)+13)%26] if letter.islower() else
              uppers[(uppers.index(letter)+13)%26] if letter.isupper() else letter 
              for letter in message]
    return ''.join(result)