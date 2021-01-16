from threading import Thread

import reciver
from utils import CONNECTIONS_LIST

Th1 = Thread(target=reciver.start)
Th1.start()
while(True):
    print(reciver.data_recv())
Th1.join()