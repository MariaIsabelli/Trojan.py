from dotenv import dotenv_values
from collections import OrderedDict
from pathlib import Path
from logging import warning, basicConfig, INFO


basicConfig(format='%(levelname)s %(asctime)s : %(message)s', level=INFO)



class Credentials(object):
    """ Objeto que recupera as variáveis de ambiente fornecidas no arquivo .env"""
    
    @staticmethod
    def get() -> OrderedDict:
        if Path('src/connection/.env').exists():
            # ENV VARIABLES: HOST, PORT
            return dotenv_values(
                dotenv_path ='src/connection/.env'
            )

        warning('Configuration file .env not found, loading default values.')