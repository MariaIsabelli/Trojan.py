import itertools

string = input("String a ser permutada: ")

resultado = itertols.permutations('string', len(string))

for i in resultado:
  print(''.join(i))
  
