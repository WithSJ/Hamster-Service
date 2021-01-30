"""
Hamster Client Service
"""
import socket
import threading

from hamster_service.connection.connector import Connector
from hamster_service.connection.utils import PORT_NUMBER


class Client(Connector,threading.Thread):
    def __init__(self):
        self.SOCKET = self.create_tcp_socket()        
    
    def connect(self,ip_address=""):
        try:
            self.SOCKET.connect((ip_address,PORT_NUMBER))
        except socket.error as msg:
            print(f"Client socket error {msg}")
    
    def send_data(self):
        """Send Data to connected Socket"""
        pass
    
    
        
