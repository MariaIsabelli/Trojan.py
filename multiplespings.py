import os 
import times

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlilines()
    
    for ip in dump:
          print('Verificando o ip: ',ip)
          print('-'*60)
         os.system('ping -n 2 {} '.fomart(ip))
         print('-'*60)
         time.sleep(5) 
          
        
          
        
    

