
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

plaintext = ''
for letter in 'TRGBSSZLYNJA':
    plaintext += shift(letter, 3, decrypt=True)
print(f'{plaintext = }')

ciphertext = 'PHHWDWWKHEULGJHDWGDZQ'
for shift_amount in range(1, 26):
    plaintext = ''
    for letter in ciphertext:
        plaintext += shift(letter, shift_amount)
    print(plaintext)

def vigenere(plaintext, key, decrypt=False):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # duplicate the key so that its length >= length of plaintext
    key += key * (len(plaintext) // len(key))

    # go char by char and shift by corresponding key char
    ciphertext = ''
    for i in range(len(plaintext)):
        shift_amount = alphabet.index(key[i]) + 1
        ciphertext += shift(plaintext[i], shift_amount, decrypt)
    return ciphertext

print(f'{vigenere('SANDWICHESAREGOOD', 'TOMATO') = }')
print(f'{vigenere('MPAEQXWWRTUGYVBPX', 'TOMATO', decrypt=True)}')
