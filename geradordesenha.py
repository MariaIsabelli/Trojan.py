import random
import string

tamanho = int(input('Digite o tamanho que vocẽ deseja para sua senha: '))

chars = string.ascii_letters_letters + string.digits + 'ç"!@#$%¨&*()_-=+,.:;/\?][{}^~´`'` 
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) fot i  in range (tamanho)))
