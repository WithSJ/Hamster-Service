import threading

# All Connected pear in this list
CONNECTIONS_LIST = list()

class Connections_Handler(threading.Thread):
    def __init__(self):
        """Handle or manage all connections in CONNECTIONS_LIST"""
        pass
    
    def run(self):
        pass

    @classmethod
    def is_connected(cls,socket):
        """Check connection is live or not."""
        pass
