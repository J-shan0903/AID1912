
from threading import Thread,Lock

n =5000

def f1():
    global n
    for i in range(1000000):
        Lock.acquire()
        n = n+1
        Lock.release()
def f2():
    global n
    for i in range(1000000):
        Lock.acquire()
        n = n-1
        Lock.acquire()

t1 = Thread(target=f1)
t1.start()

t2 =Thread(target=f2)
t2.start()

t1.join()
t2.join()
print(n)