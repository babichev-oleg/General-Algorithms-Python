#!/usr/bin/python3.6
import os
from multiprocessing import Process
def doubler(number):
    result = number ** 2000000000000000000000
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))
if __name__ == '__main__':
    numbers = [88888888888, 9999999999, 7777777777, 3333333333, 5555555555]
    procs = []
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

