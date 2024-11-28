def shift(letter, shift_amount, decrypt = False):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_index = alphabet.index(letter)
    if decrypt:
        letter_index -= shift_amount
        if letter_index < 0:
            letter_index += len(alphabet)
    else:
        letter_index += shift_amount
        if letter_index >= len(alphabet):
            letter_index -= len(alphabet)
    return alphabet[letter_index]

print(f'{shift("A", 5) = }')
print(f'{shift("A", 5, decrypt=True) = }')
print(f'{shift("X", 5) = }')
print(f'{shift("X", 5, decrypt=True) = }')

ciphertext = 'TRGBSSZLYNJA'
plaintext = ''
for letter in ciphertext:
    plaintext += shift(letter, 3, decrypt=True)
print(f'{plaintext = }')

ciphertext = 'PHHWDWWKHEULGJHDWGDZQ'
for shift_amount in range(1, 26):
    plaintext = ''
    for letter in ciphertext:
        plaintext += shift(letter, shift_amount, decrypt=True)
    print(plaintext)

def vigenere(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key += key * (len(plaintext) // len(key))
    ciphertext = ''
    for i in range(len(plaintext)):
        shift_amount = alphabet.index(key[i]) + 1
        ciphertext += shift(plaintext[i], shift_amount)
    return ciphertext

print(f'{vigenere("THEPACKAGEISUNDERTHETREE", "BOSCO")}')