import ctypes 

pasta = input("Digite o caminho da pasta a ser ocultada:")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('Ocultar.txt', atributo_ocultar)

if retorno:
  print("Arquivo foi ocultado")
 else:
    print("Arquivo não ocultado")
    
    
