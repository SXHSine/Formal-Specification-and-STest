import time
from multiprocessing import Process, current_process
import threading

def foo(i):
    print(str(i))

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.start()