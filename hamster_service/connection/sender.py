"""
Hamster Sender Service
"""
import socket
from hamster_service.connection.connector import Connector
from hamster_service.protocol import PORT_NUMBER

class Sender(Connector):

    def __init__(self,socket_type="tcp",socket=None):
        """
        [socket_type] should be a string of protocol it can be TCP or UDP.
        [socket] if you have socket you can use it.
        """
        self.SOCKET = socket
        
        if socket == None and socket_type.lower() == "tcp":
            self.SOCKET = self.create_tcp_socket()
        elif socket == None and socket_type.lower() == "udp":
            self.SOCKET = self.create_udp_socket()
    
    def connect_tcp_socket(self,server_ip=""):
        """Connect to pear and return socket object for send recive data"""
        try:
            self.SOCKET.connect((server_ip,PORT_NUMBER))
            return self.SOCKET
        except socket.error as msg:
            raise RuntimeError(f"TCP Socket Connecting error {msg}") 
 