import hashlib

arquivo1 = 'arquivo.txt'
arquivi2 = 'arquivo2.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
  print(f'O arquivo: {arquivo1}  é difentente do {arquivo2}')
  print('O hash do arquivo arquivo1.txt é', hash1.hexdigest())
  print('O hash do arquivo arquivo2.txt é', hash2.hexdigest())
else:
  print  print(f'O arquivo: {arquivo1}  é igual o {arquivo2}')
  print('O hash do arquivo arquivo1.txt é', hash1.hexdigest())
  print('O hash do arquivo arquivo2.txt é', hash2.hexdigest())
    
    
