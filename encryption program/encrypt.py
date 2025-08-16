import string
import  random

chars = '' + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT
plain_text = input('Enter the message you want to encrypt: ')
chiper_text = ''

for letter in plain_text:
    index = chars.index(letter)
    chiper_text += key[index]

print(f'Original messages: {plain_text}')
print(f'Encypted messages: {chiper_text}')

#DECRYPT
chiper_text = input('Enter the encrypted message to be converted to normal: ')
plain_text = ''

for letter in chiper_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f'Encypted messages: {chiper_text}')
print(f'Original messages: {plain_text}')