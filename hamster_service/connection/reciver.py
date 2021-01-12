"""
Hamster Revicer Service
"""
import socket
from hamster_service.connection.connector import Connector
from hamster_service.connection.utils import CONNECTIONS_LIST
from hamster_service.protocol import BUFFER_SIZE,PORT_NUMBER
from hamster_service.connection.utils import HOST_IP,Connection_OBJ


class Revicer(Connector):
    pass