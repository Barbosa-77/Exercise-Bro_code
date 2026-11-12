# Encryption Program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key= chars.copy()

random.shuffle(key)

while True:
    print("1 - Encrypt")
    print("2 - Decrypt")
    acao = int(input("Choose a action: \n"))
    #Encrypt
    match acao:
        case 1:
            plain_text = input("Enter a message to encrypt: \n")
            cipher_text = ""

            for letter in plain_text:
                index = chars.index(letter)
                cipher_text += key[index]

            print(f"Original message: {plain_text}")
            print(f"Encrypted message: {cipher_text}")

    #Decrypt
        case 2:
            cipher_text = input("Enter a message to encrypt: \n")
            plain_text = ""

            for letter in cipher_text:
                index = key.index(letter)
                plain_text += chars[index]

            print(f"Encrypted message: {cipher_text}")
            print(f"Original message: {plain_text}")
        case 0:
            break