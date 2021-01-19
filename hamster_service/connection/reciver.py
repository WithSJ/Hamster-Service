"""
Hamster Revicer Service
"""
import socket

from hamster_service.connection.connector import Connector
from hamster_service.connection.utils import (BUFFER_SIZE, CONNECTIONS_LIST,
                                              HOST_IP, PORT_NUMBER,
                                              Connection_OBJ)


class Reciver(Connector):
    
    def __init__(self):
        self.SOCKET = self.create_tcp_socket()
        self.SOCKET.bind((HOST_IP(),PORT_NUMBER))
    
    def start(self):
        """
        Start Revicer
        """
        self.SOCKET.listen(5)
        while True:
            conn,ip_port = self.SOCKET.accept()
            obj = Connection_OBJ(connection=conn,ip_port=ip_port)
            CONNECTIONS_LIST.append(obj)
    
    def stop(self):
        """
        Stop Revicer
        """
        self.SOCKET.close()

    def recive_data(self):
        """Recive Data from connected Socket and close connection."""
        pass
    