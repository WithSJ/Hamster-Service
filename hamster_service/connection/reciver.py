"""
Hamster Revicer Service
"""
import socket
from hamster_service.connection.connector import Connector
from hamster_service.connection.utils import CONNECTIONS_LIST
from hamster_service.protocol import BUFFER_SIZE,PORT_NUMBER
from hamster_service.connection.utils import HOST_IP


class Revicer(Connector):
    
    def __init__(self,socket_type="tcp",socket=None):
        """
        [socket_type] should be a string of protocol it can be TCP or UDP
        [socket] if you have socket you can use it
        """
        self.SOCKET = socket
        
        if socket == None and socket_type.lower() == "tcp":
            self.SOCKET = self.create_tcp_socket()
        elif socket == None and socket_type.lower() == "udp":
            self.SOCKET = self.create_udp_socket()
    
    def bind_tcp_socket(self):
        """Bind Host and port and start listening"""
        try:
            self.SOCKET.bind((HOST_IP,PORT_NUMBER))
            self.SOCKET.listen(5)
        except socket.error as msg:
            raise RuntimeError(f"TCP Socket Binding error {msg}") 


    def tcp_socket_accept(self):
        """Accept connection and return it for send recive data"""
        try:
            conn = self.SOCKET.accept()
            return conn
        except socket.error as msg:
            raise RuntimeError(f"TCP Socket Accepting error {msg}") 
        
    def start(self):
        """
        accept connection and add in Connection List
        """
        while True:
            conn = self.tcp_socket_accept()
            self.check_in_conn_list(conn)

    def check_in_conn_list(self,conn):
        """
        Check this connecction already in Connection List or not
        if Connection ip already than don't add this 
        if new conncetion have diffrent ip than older so remove 
        old one and new one.
        """
        # till now we dont use username when username we use we add this 
        #  {"socket_type":"tcp","username":conn_obj} in Connection_list
        
        insert_it = True
        for ConnList in CONNECTIONS_LIST:
            if conn[1][0] == ConnList[1][0]:
                insert_it = False

        if insert_it:                
            CONNECTIONS_LIST.append(conn)


