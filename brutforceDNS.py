import dns.resolver, socket, readline
from datetime import datetime

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

print ("\nDigite o caminho da wordlist com subdomínios: ")

arquiv = input()
arquivo = open(arquiv,'r')

subdominios = arquivo.read().splitlines()

print ("\nDigite o domínio: ")
alvo = input()

print ("\nDigite o caminho com o nome do arquivo para exportar o resultado ('Exemplo: /home/user/Documentos/resultadodobrutforceDNS.txt'): ")
nomedoarquivo = input()

print("\nIniciado em: "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\n")

for subdominio in subdominios:

    try:
        sub_alvo = subdominio + "." + alvo
        
        resultado = dns.resolver.resolve(sub_alvo,"A")
        
        if resultado:
            
            ip = socket.gethostbyname(sub_alvo)         
            
            print(sub_alvo + " -> " + ip)
            
            paraexportar = sub_alvo + " -> " + ip + "\n"
            
            with open(nomedoarquivo,'a') as exportar:
                exportar.write(paraexportar)
            
        else:
            pass
            
    except socket.gaierror:
        pass
        
    except dns.resolver.LifetimeTimeout:
        pass
        
    except dns.resolver.NXDOMAIN:
        pass
        
    except dns.resolver.NoAnswer:
        pass 

    except KeyboardInterrupt:
        quit()
    
print("\nFinalizado em: "+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\n")
