import soket
import sys

def main():
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
  except socket.error as error: 
    print("A conexao falhou")
    print("ERRO: {}".format(error))
    
    sys.exit()
  print("Connect")
  
  HostAlvo = input("Digite o Host ou IP que deseja conectar: ")
  PortaAlvo = input("Digite a porta que deseja conectar: ")
  
  try:
    s.connect((HostAlvo, int(PortaAlvo)))
    print("Cliente TCP conectado com Sucesso no Host:" + HostAlvo + "e na porta:" + PortaAlvo)
    s.shutdown(2)
    
 except socket.error as error:
    print("Conexao falha, ERROR")
    print("ERROR: {}".fomart(error))
    sys.exit()
    
 if __name__ == "__main__":
    main()
    
  
  
  
