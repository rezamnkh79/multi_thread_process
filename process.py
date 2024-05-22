import os
from multiprocessing import Process, current_process, Queue


def show(name, index):
    print(f"start thread {name}\n")
    while index < 10:
        index += 1
        print(str(index) + "\n")
        print(current_process())
        print(os.getpid())  # current process pid
        print(os.getppid())  # parent pid
    print(f"end thread {name}\n")


# i = 0
# p1 = Process(target=show, args=('p1', i,))
# p2 = Process(target=show, args=('p2', i,))
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
#
# print("finish")

l = []


def p1_func():
    global l
    l.append([1, 2, 3])
    print(l)


def p2_func():
    global l
    l.append([4, 5, 6])
    print(l)


# p1 = Process(target=p1_func)
# p2 = Process(target=p2_func)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()
# print(l)
# ===============================================================
# resolve for above problem

l = []


def p1_func(queue):
    num = queue.get()
    num.extend([1, 2, 3])
    queue.put(num)
    print(num)


def p2_func(queue):
    num = queue.get()
    num.extend([4, 5, 6])
    queue.put(num)
    print(num)


queue = Queue()
queue.put(l)
p1 = Process(target=p1_func, args=(queue,))
p2 = Process(target=p2_func, args=(queue,))

p1.start()
p2.start()
p1.join()
p2.join()
print(queue.get())
