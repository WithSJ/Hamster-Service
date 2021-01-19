# Start Hamster Service using threading 

from threading import Thread

from hamster_service.connection.reciver import Reciver

# create reciver thread 
reciver_thread = Thread(target=Reciver.start)

recive_request = Thread(target=Reciver.recive_request)




