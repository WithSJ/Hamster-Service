from threading import Thread
from utils import CONNECTIONS_LIST
import reciver
Th1 = Thread(target=reciver.start)
Th1.start()
while(True):
    print(reciver.data_recv())
Th1.join()