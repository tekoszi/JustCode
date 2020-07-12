import string
uppercaseletters = string.ascii_uppercase
lowercaseletters = string.ascii_lowercase
offset = 23

def cipher(string):
    global offset
    ciphered = ''
    for char in string:
        try:
            if char.isupper():
                ciphered += uppercaseletters[uppercaseletters.index(char) + offset]
            else:
                ciphered += lowercaseletters[lowercaseletters.index(char) + offset]
        except:
            if char.isupper():
                ciphered += uppercaseletters[(uppercaseletters.index(char) + offset) % 26 if (uppercaseletters.index(char) + offset) > 25 else uppercaseletters.index(char) + offset]
            else:
                ciphered += lowercaseletters[(lowercaseletters.index(char) + offset) % 26 if (lowercaseletters.index(char) + offset) > 25 else lowercaseletters.index(char) + offset]
    return ciphered

def decipher(cipher):
    global offset
    deciphered = ''
    for char in cipher:
        try:
            if char.isupper():
                deciphered += uppercaseletters[uppercaseletters.index(char) - offset]
            else:
                deciphered += lowercaseletters[lowercaseletters.index(char) - offset]
        except:
            offset %= 26
            print(offset)
            if char.isupper():
                deciphered += uppercaseletters[(uppercaseletters.index(char) - offset) % -26 if (uppercaseletters.index(char) - offset) > 25 else uppercaseletters.index(char) - offset]
            else:
                deciphered += lowercaseletters[(lowercaseletters.index(char) - offset) % -26 if (lowercaseletters.index(char) - offset) > 25 else lowercaseletters.index(char) - offset]
    return deciphered


with open('dane.txt') as f:
    read_data = f.read().split('\n')


# for word in read_data:
#     print(decipher(word))
#
# for word in read_data:
#     print(cipher(word))