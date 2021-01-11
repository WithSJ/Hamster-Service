"""
All basic utility are here  for Hamster Network Service
"""
import socket
from hamster_service.protocol import PORT_NUMBER


#Host ip address for creating server
HOST_IP = ""

# All Connected pear in this list
CONNECTIONS_LIST = list()

class Connection():
    def __init__(self):
        self.SOCKET=None   
        
    def create_tcp_socket(self):
        """ Connecton orented protocol  """
        try:    
            
            self.SOCKET = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)

        except socket.error as msg:
            raise RuntimeError(f"Socket creation error {msg}")

    # def create_udp_socket(self):
    #     """ NON-Connecton orented protocol more faster than tcp  """
    #     try:
    #         global SOCKET
    #         SOCKET = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
    #     except socket.error as msg:
    #         return f"Socket creation error {msg}"

    def bind_socket(self):
        """Bind Host and port and start listening"""
        try:
            self.SOCKET.bind((HOST_IP,PORT_NUMBER))
            self.SOCKET.listen(5)
        except socket.error as msg:
            raise RuntimeError(f"Socket Binding error {msg}") 


    def socket_accept(self):
        """Accept connection and return it for send recive data"""
        try:
            conn = self.SOCKET.accept()
            return conn
        except socket.error as msg:
            raise RuntimeError(f"Socket Accepting error {msg}") 

    def connect_socket(self,server_ip="",port=PORT_NUMBER):
        """Connect to pear and return socket object for send recive data"""
        try:
            self.SOCKET.connect((server_ip,port))
            return self.SOCKET
        except socket.error as msg:
            raise RuntimeError(f"Socket Connecting error {msg}") 
            
    def get_my_ip(self):
        """return current system ip address """
        self.create_tcp_socket()
        return self.connect_socket("google.com",80)
        
        