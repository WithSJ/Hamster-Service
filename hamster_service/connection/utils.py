"""
All basic utility are here  for Hamster Network Service
"""


#Host ip address for creating server
HOST_IP = ""

# All Connected pear in this list
CONNECTIONS_LIST = list()


class Connection_OBJ:
    def __init__(self, connection=None,ip_port=None,username=None,socket_type=None):
        """
        Connected obj data store in this class object 
        """
        self.conntion = connection
        self.ip_port = ip_port
        self.username = username
        self.socket_type = socket_type
    
