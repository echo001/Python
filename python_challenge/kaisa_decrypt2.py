#kaisa decrypt: K——>M  O——>Q  F——>G
import string
words = input('Enter you want to decrypt: ')
#decrypt_word = ''

decrypt_word = words.translate(words.maketrans(string.ascii_lowercase,'cdefghijklmnopqrstuvwxyzab'))

print('\n' + decrypt_word)
