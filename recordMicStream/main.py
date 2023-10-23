#!/usr/bin/python3
# coding: utf-8

__author__ = '@zNairy'
__contact__ = 'zNairy#7181 | www.github.com/zNairy'
__version__ = '1.0'

from src.server import ServerManager
from src.connection.credentials import Credentials


def main():
    credentials = Credentials.get()
    
    if credentials:
        server = ServerManager(
            hostName = credentials.get('HOST'),
            portNumber = int(credentials.get('PORT'))
        )

    else:
        server = ServerManager()

    server.run()



if __name__ == '__main__':
    main()