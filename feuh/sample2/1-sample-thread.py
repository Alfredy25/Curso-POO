import time

from feuh.sample2.thread.name_thread import NameThread

thread1 = NameThread('John Doe')
thread1.start()
# time.sleep(1 / 10000)
thread2 = NameThread('Alfredo Hernandez')
thread2.start()

thread3 = NameThread('Maria Roe')
thread3.start()
print(f'Thread is alive {thread1.is_alive()}')