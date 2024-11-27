'meetmeattheclocktoweratseven'
'PHHW...'

def shift(letter, shift_amount):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_index = alphabet.index(letter)
    letter_index += shift_amount
    letter_index = letter_index % len(alphabet)
    if letter_index < 0:
        letter_index += len(alphabet)
    return alphabet[letter_index]

ciphertext = 'PHHWDWWKHEULGJHDWGDZQ'
for shift_amount in range(1, 26):
    plaintext = ''
    for letter in ciphertext:
        plaintext += shift(letter, -shift_amount)
    print(f'{plaintext = }')

def vigenere(plaintext, key, decrypt = False):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key += key * (len(plaintext) // len(key))
    ciphertext = ''
    for i in range(len(plaintext)):
        shift_amount = alphabet.index(key[i]) + 1
        if decrypt:
            shift_amount *= -1
        ciphertext += shift(plaintext[i], shift_amount)
    return ciphertext

print(f'{vigenere('PACKAGEDELIVERED', 'ABC') = }')
print(f'{vigenere('QCFLCJFFHMKYFTHE', 'ABC', decrypt = True) = }')
