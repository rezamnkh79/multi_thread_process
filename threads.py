from threading import Thread, Lock, RLock, Semaphore, BoundedSemaphore
from time import sleep

lock = Lock()
lock = Lock()
lock = RLock()
lock = Semaphore(value=2)
lock = BoundedSemaphore()


def show(name, index):
    print(f"start thread {name}\n")
    lock.acquire()
    while index < 10:
        index += 1
        print(str(index) + "\n")
    lock.release()
    print(f"end thread {name}\n")


index = 0
thread1 = Thread(target=show, args=(1, index,))
thread2 = Thread(target=show, args=(2, index,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

num = 0


def add():
    global num
    with lock:
        while num < 100:
            num += 1
            print(num)


thread3 = Thread(target=add())
thread4 = Thread(target=add())

thread3.start()
thread4.start()
