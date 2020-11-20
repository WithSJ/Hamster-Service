import socket
from protocol import HOST_IP,PORT_NUMBER,CONNECTIONS_LIST

def create_tcp_socket():
    """ Connecton orented protocol  """
    try:    
        global SOCKET
        SOCKET = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
    except socket.error as msg:
        return f"Socket creation error {msg}"

# def create_udp_socket():
#     """ NON-Connecton orented protocol more faster than tcp  """
#     try:
#         global SOCKET
#         SOCKET = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
#     except socket.error as msg:
#         return f"Socket creation error {msg}"

def bind_socket():
    """Bind Host and port and start listening"""
    try:
        global SOCKET
        SOCKET.bind((HOST_IP,PORT_NUMBER))
        SOCKET.listen(5)
    except socket.error as msg:
        return f"Socket Binding error {msg}"


def socket_accept():
    """Accept connection and return it for send recive data"""
    try:
        global SOCKET
        conn = SOCKET.accept()
        return conn
    except socket.error as msg:
        return f"Socket Accepting error {msg}"

def connect_socket(server_ip=""):
    """Connect to pear and return socket object for send recive data"""
    try:
        global SOCKET
        SOCKET.connect((server_ip,PORT_NUMBER))
        return SOCKET
    except socket.error as msg:
        return f"Socket Connecting error {msg}"
        
