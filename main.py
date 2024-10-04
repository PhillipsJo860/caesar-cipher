# Joshua Phillips
# 10/4/24
# Caesar Cipher encription practice

'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''

user_message = input('Enter secret message here: ').lower()
key = int(input('Enter your desired key: '))
# print(user_message)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

    else:
        new_message += character

print(f'Your new message is {new_message}')
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''

user_message = input('Enter secret message here: ').lower()
key = int(input('Enter your desired key: '))
# print(user_message)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

    else:
        new_message += character

print(f'Your new message is {new_message}')