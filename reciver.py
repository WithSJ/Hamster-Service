"""
Reciver Funtions are define here
"""
from utils import Connection,CONNECTIONS_LIST
from protocol import BUFFER_SIZE

def start():
    """
    Start Reciver server accept connection and add them in Connection list
    """
    conn = Connection()
    conn.create_tcp_socket()
    conn.bind_socket()
    
    while True:
        conn_obj=conn.socket_accept()
        CONNECTIONS_LIST.append(conn_obj)

def data_recv():
    """
    recive data from all connection one by one
    """
    Data_Recived=list()
    for conn in CONNECTIONS_LIST:
        data = conn[0].recv(BUFFER_SIZE)
        if not data:
            Data_Recived.append((data,conn[1]))
             
    return Data_Recived
        
            









# def all_conn():
#     print(CONNECTIONS_LIST)
        