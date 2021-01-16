"""
Hamster Sender Service
"""
import socket

from hamster_service.connection.connector import Connector
from hamster_service.connection.utils import PORT_NUMBER


class Sender(Connector):
    def __init__(self):
        self.SOCKET = self.create_tcp_socket()        
    
    def connect(self,ip_address=""):
        self.SOCKET.connect((ip_address,PORT_NUMBER))
    
    def send_data(self):
        """Send Data to connected Socket"""
        pass
    
    
        
