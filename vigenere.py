def shift(char, key_char, decrypt=False):
    if not char.isalpha():
        return char
    base = ord('A')
    offset = ord(key_char.upper()) - base
    if decrypt:
        offset = -offset
    return chr((ord(char.upper()) - base + offset) % 26 + base)

def vigenere(text, key, decrypt=False):
    result = []
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            result.append(shift(char, key[key_index % len(key)], decrypt))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def encrypt(text, key):
    return vigenere(text, key, decrypt=False)

def decrypt(text, key):
    return vigenere(text, key, decrypt=True)
