"""
All basic utility are here  for Hamster Network Service
"""
from hamster_service.connection.connector import Connector


#All Sercives work on this port
PORT_NUMBER = 2020   

#Buffer size IN 250 BYTES FOR RECIVE AND SEND DATA AT ONE TIME
BUFFER_SIZE = 250

#Host ip address for creating server
def HOST_IP():
    """get host ip address """
    soc = Connector().create_tcp_socket()
    soc.connect(("google.com",80))
    ip = soc.getsockname()[0]
    soc.close()
    return ip
    

# All Connected pear in this list
CONNECTIONS_LIST = list()


class Connection_OBJ:
    def __init__(self, connection=None,ip_port=None,username=None,socket_type=None):
        """
        Connected obj data store in this class object 
        """
        self.connection = connection
        self.ip_port = ip_port
        self.username = username
        self.socket_type = socket_type
        
    
