#!/usr/bin/python3.7
import time
from typing import Dict
memo: Dict[int, int] = {0: 0,1: 1}
start_time = time.time()
def fibonacci(n: int) -> int:
    if n not in memo:
        memo[n] = fibonacci(n-1)+fibonacci(n-2) 
    return memo[n]
if __name__ == "__main__":
    print(fibonacci(3))
    print(fibonacci(50))
print("--- %s seconds ---" % (time.time() - start_time))
