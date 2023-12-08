from threading import current_thread, Thread
from time import sleep

def daemon_func():
    print(current_thread().daemon)
    sleep(3)
    print('{}: Hello from daemon'.format(current_thread().name))

def nondaemon_func():
    print(current_thread().daemon)
    sleep(1)
    print('{}: Hello from non-daemon'.format(current_thread().name))
    
t1 = Thread(target=daemon_func, name='Daemon thread', daemon=True)
t2 = Thread(target=nondaemon_func, name='Non-Daemon thread')

t1.start()
t2.start()

t1.join()

print('Exiting the main program')
