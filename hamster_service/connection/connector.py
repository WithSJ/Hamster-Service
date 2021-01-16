import socket
class Connector():
    def __init__(self):
        self.SOCKET=None   
        
    def create_tcp_socket(self):
        """ return TCP Connecton orented protocol SOCKET OBJ  """
        
        try:    
            self.SOCKET = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
            return self.SOCKET
        except socket.error as msg:
            raise RuntimeError(f"TCP Socket creation error {msg}")

    def create_udp_socket(self):
        """ return UDP NON-Connecton orented protocol (more faster than tcp)  SOCKET OBJ """
        
        try:
            self.SOCKET = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
            return self.SOCKET
        except socket.error as msg:
            return f"UDP Socket creation error {msg}"
    
    def socket_ip_port(self):
        """Return Socket IP address and Port number"""
        return self.SOCKET.getsockname()