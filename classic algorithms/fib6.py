#!/usr/bin/python3.7
from typing import Generator
import time
start_time=time.time()
def fibonacci(n: int) -> Generator[int,None,None]:
    yield 0
    if n > 0: yield
    last : int = 0
    next : int = 1
    for _ in range(1,n):
        last, next =next, last + next
        yield next

if __name__ == "__main__":
    for i in fibonacci(50):
        print(i)
print("--- %s seconds ---" % (time.time() - start_time))
