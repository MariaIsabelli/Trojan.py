import re
import json
import wrllib.request import urlopen

url = '**url**'

resposta = urlopen(url)

dados = json.load(resposta)
ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados = ['country']
regiao = dados['regiao']

print('Detalhes do seu IP externo\n')
print('IP: [4}\nRigiao: {1}\nPais: {2}\n cidade: {3}\nOrg: {0}'.format(org,regiao,pais,cid,ip))   
      
