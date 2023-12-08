from threading import current_thread, Thread
from time import sleep

def print_hello():
    sleep(3)
    print('{}: Hello'.format(current_thread().name))

def print_message(msg):
    sleep(1.5)
    print('{}:{}'.format(current_thread().name, msg))

t1 = Thread(target=print_hello, name='Th 1')
t2 = Thread(target=print_hello, name='Th 2')
t3 = Thread(target=print_message, args=['Good morning'], name='Th 3')

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
