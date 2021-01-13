"""
Hamster Sender Service
"""
import socket
from hamster_service.connection.connector import Connector
from hamster_service.protocol import PORT_NUMBER

class Sender(Connector):
    def __init__(self):
        self.SOCKET = self.create_tcp_socket()        
    
    def connect(self):
        self.SOCKET.connect(("",PORT_NUMBER))
