from logging import basicConfig, INFO, error, info, warning
from socket import socket as Socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, gaierror
from json import loads
from sounddevice import RawOutputStream
from pynput.keyboard import Listener, KeyCode

basicConfig(format='%(levelname)s %(asctime)s : %(message)s', level=INFO)


class ServerManager(object):
    def __init__(self, hostName:str = '0.0.0.0', portNumber:int = 5000) -> None:
        self.hostName = hostName
        self.portNumber = portNumber

    def checkStopMicStreamKey(self, key):
        if isinstance(key, KeyCode):
            if key.char == 'q':
                self.clientIdentifier['connection'].send(b'micstreamstop')
                self.keyboardListener.stop()    
    
    def receiveMicStreamFrames(self):
        info("Starting listener of Microphone Streaming")

        self.keyboardListener = Listener(on_press=self.checkStopMicStreamKey)
        self.keyboardListener.start()

        microphoneStream = RawOutputStream(channels=2, samplerate=44100)
        microphoneStream.start()
        
        info("Microphone Streaming started, if you want to stop press letter 'Q'")

        while True:
            try:
                currentFrame = self.clientIdentifier['connection'].recv(32768)
            
            except KeyboardInterrupt:
                break

            if currentFrame != b'micstreamstop':
                try:
                    microphoneStream.write(currentFrame)

                except Exception as err:
                    microphoneStream.stop()
                    self.keyboardListener.stop()
                    self.clientIdentifier['connection'].close()
                    error(err) & exit(1)

            else:
                warning("Stopping Microphone streaming")
                microphoneStream.stop()
                break
        
        info("Microphone streaming stopped")

        self.clientIdentifier['connection'].close()

    def __configureSocket(self) -> Socket:
        info("Configuring socket to bind")
        
        try:
            newSocket = Socket(
                family=AF_INET,
                type=SOCK_STREAM
            )

            newSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

            newSocket.bind(
                (self._hostName, self._portNumber)
            )

            newSocket.listen(1)

        except OverflowError:
            error(f'"{self._portNumber}" Port too large, must be in range 0-65535') & exit(1)
        except OSError:
            error(f'"{self._hostName}" Cannot assign requested address') & exit(1)
        except gaierror:
            error(f'"{self._hostName}" Name or service not known') & exit(1)

        return newSocket

    def run(self):
        socket = self.__configureSocket()

        info(f"Starting and listening server manager on [{self._hostName}:{self._portNumber}]")

        clientConnection, address = socket.accept()

        self.clientIdentifier = loads(clientConnection.recv(1024).decode('utf-8'))

        self.clientIdentifier.update({
            "connection": clientConnection,
            "address": address
        })

        info(f"Incoming connection from [{self.clientIdentifier['username']}:{self.clientIdentifier['hostname']}] | [{self.clientIdentifier['address'][0]}:{self.clientIdentifier['address'][1]}]")
        
        self.receiveMicStreamFrames()

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