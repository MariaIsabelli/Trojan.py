import subprocess, sys, platform, os

sistemaoperacional = platform.system()

if sistemaoperacional == "Windows":

    try:
        meta_data = subprocess.check_output(['netsh','wlan','show','profiles'])

    except:
        sys.exit(1)

    data = meta_data.decode('utf-8', errors = "backslashreplace")
    data = data.split('\n')
    profiles = []

    for i in data:
        if "All User Profile" in i:
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            profiles.append(i)

    print("{:<30}| {:<}".format("NOME DA WI-FI", "SENHA DA WI-FI"))
    print("_____________________________________________")

    for i in profiles:

        nomedowifi = "name=" + i       

        try:

            results = subprocess.check_output(['netsh','wlan','show','profile',nomedowifi,'key=clear'])
            results = results.decode('utf-8', errors = "backslashreplace")
            results = results.split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b ]

            print("{:<30}| {:<}".format(i, results[0]))

        except IndexError:
            print("{:<30}| {:<}".format(i,""))                                  

        except subprocess.CalledProcessError:
            pass

elif sistemaoperacional == "Linux":

    if not 'SUDO_UID' in os.environ:
        print("Você não tem permissões de ROOT e/ou faz parte do SUDO, execute novamente com \"sudo\" ou como ROOT!")

    else:
        print("{:<30}| {:<}".format("NOME DA WI-FI", "SENHA DA WI-FI"))
        print("_____________________________________________")

        comando = '^psk='

        try:
            resultado = subprocess.check_output(['grep', '-r', comando, '/etc/NetworkManager/system-connections/']) #É necessário um USER "elevado" para leitura dentro do /etc/NetworkManager/*/
            resultado = resultado.decode('utf-8', errors = "backslashreplace")
            resultado = resultado.replace("/etc/NetworkManager/system-connections/",",").replace(".nmconnection:","").replace("psk=",",| ").replace("\n","")
            resultado = resultado.split(",")
            impar = resultado[1::2]
            par = resultado[2::2]
            redesenha = "\n".join("{:<29} {:3}".format(x, y) for x, y in zip(impar, par))
            print(redesenha)

        except subprocess.CalledProcessError:
            print("\nDesculpe, não encontrei nenhuma rede wi-fi!") 
            sys.exit(1)            

else:
    print("Estamos trabalhando para suportar esse sistema operacional! Por favor, abra um \"issue\" no github e nos informe qual é o sistema que você está utilizando.")
