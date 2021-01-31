"""
Hamster Server Service
"""
import socket
import threading

from hamster_service.connection.connector import Connector
from hamster_service.connection.handler import CONNECTIONS_LIST
from hamster_service.connection.utils import (BUFFER_SIZE,HOST_IP, PORT_NUMBER,
                                              Connection_OBJ)
                                        


class Server(Connector,threading.Thread):
    
    def __init__(self):
        self.SOCKET = self.create_tcp_socket()
        self.SOCKET.bind((HOST_IP(),PORT_NUMBER))
        threading.Thread.__init__(self)
        
    def run(self):
        """
        Start Server in Thread
        """
        self.daemon = False 
        # use True if you want to run thread after program closed
        
        self.SOCKET.listen(5)
        while True:
            conn,ip_port = self.SOCKET.accept()
            obj = Connection_OBJ(connection=conn,ip_address=ip_port[0])
            CONNECTIONS_LIST.append(obj)
    
    def stop(self):
        """
        Stop Server connection and Thread
        """
        self.SOCKET.close()
        self.join()
