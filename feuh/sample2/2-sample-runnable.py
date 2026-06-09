from threading import Thread
from feuh.sample2.thread.travel_task import TravelTask

thread1 = Thread(target=TravelTask('Isla de Pascua').arrancar)
thread1.start()
Thread(target=TravelTask('Islas Malvidas').arrancar).start()
Thread(target=TravelTask('Isla Juan Fernandez').arrancar).start()
Thread(target=TravelTask('Isla de Chiloe').arrancar).start()
Thread(target=TravelTask('Isla Robinson Crusoe').arrancar).start()