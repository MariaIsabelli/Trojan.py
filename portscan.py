import socket 
import sys

ports= [21,22,80,443,445,3306,25,7777]

for port in  ports:
        try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.1)
                code = client.connect_ex((sys.argv[1],port))
                if code == 0:
                        print(port,"Open")
                else: 
                        print(port,"Closed")
                client.close()
        except:
                print(port,'Closed')

