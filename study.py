# from threading import Thread, Lock

# def inc(lock):
#     global x
#     for i in range(1000000):
#         lock.acquire()
#         x += 1
#         lock.release()
        
# mylock = Lock()

# x = 0

# t1 = Thread(target=inc, args=(mylock,), name="Th 1")
# t2 = Thread(target=inc, args=(mylock,), name="Th 2")

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print('Final value of x:', x)

