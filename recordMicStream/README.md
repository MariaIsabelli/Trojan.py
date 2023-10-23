# Record Microphone Stream

![badges](https://img.shields.io/badge/Python-v3.8-red)

Trasmite ao vivo o áudio do microfone, via socket.



## Instalação
Baixe ou clone o repositório usando:
```bash
git clone https://github.com/zNairy/ferramentas_pentest
```
ou
```bash
git clone https://github.com/MariaIsabelli/ferramentas_pentest
```

Em seguida instale os recursos necessários descritos em <b>requirements</b>, utilizando o pip de acordo com sua versão do Python.
```bash
python -m pip install -r requirements.txt
```
## Como usar
Inicie o lado servidor com <tt>python main.py</tt> para iniciar o gerenciador que escutará possíveis conexões do lado cliente. Por padrão, tanto o servidor quanto cliente é conectado no endereço <tt>0.0.0.0:5000</tt> se nenhum argumento for passado em sua instância. 

```python
class ServerManager(object):
    def __init__(self, hostName:str = '0.0.0.0', portNumber:int = 5000) -> None:
```

Para inferir esses parâmetros de host e porta, crie um arquivo `.env` no diretório ´recordMicStream/src/connection/´ e passe a seguinte estrutura, como por exemplo, e o utilitário assumirá os novos parâmetros como variáveis de ambiente:

```env
HOST=127.0.0.1
PORT=5001
```

Em seguida para inicializar o lado servidor e começar a escutar conexões, rode
```bash
python main.py
```

do lado cliente apenas execute
```bash
python src/client.py
```


A transmissão começará manualmente, se quiser parar o processo pressione a letra 'Q' no teclado e ele se encerrará.