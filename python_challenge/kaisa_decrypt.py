#kaisa decrypt: K——>M  O——>Q  F——>G
import string
'''
def decrypt(alpha):
    num = ord(alpha)
    num = num + 2
    return chr(num)
'''
words = input('Enter you want to decrypt: ')
decrypt_word = ''
for word in words:
    found_postion = string.ascii_lowercase.find(word)
    if (found_postion == -1):
        decrypt_word = decrypt_word + word
        continue
    if (found_postion >= 24):
        found_postion -= 24
        decrypt_word += string.ascii_lowercase[found_postion]
        continue
    decrypt_word += string.ascii_lowercase[found_postion+2]
#    if (found_postion)
#    alpha = decrypt(word)
#    decrypt_word = decrypt_word + alpha
print('\n' + decrypt_word)
