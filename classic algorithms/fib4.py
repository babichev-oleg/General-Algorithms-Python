#!/usr/bin/python3.7
import time
from functools import lru_cache
start_time=time.time()
@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2) 

if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(500))
print("--- %s seconds ---" % (time.time() - start_time))
