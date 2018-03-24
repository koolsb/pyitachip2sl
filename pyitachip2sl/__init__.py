import socket
import logging

_LOGGER = logging.getLogger(__name__)


class ITachIP2SLSocketClient(object):
    """
    Python client for the iTach IP2SL Socket server
    """

    _socket_recv = 1024

    def __init__(self, host, port=4999, timeout=1):
        """
        Initialize the socket client.
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(timeout)
        self.socket.connect((self.host, self.port))

    def send_data(self, data):
        """
        Send data to socket.
        """
        if data.startswith('0x'):
            data = bytes.fromhex(data[2:].rstrip())
        else:
            data = data.encode('ascii')

        _LOGGER.debug("Sending data: " + str(data))
        self.socket.send(data)

        try:
            response = self.socket.recv(self._socket_recv)
            _LOGGER.debug("Received response: " + str(response))

            return response.decode('ascii').strip()
        
        except socket.timeout as e:
            _LOGGER.debug("Socket timeout. Error: " + str(e))
            return 
