!/usr/bin/python3.7
import time
start_time = time.time()
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
if __name__ == "__main__":
    print(fibonacci(35))
print("--- %s seconds ---" % (time.time() - start_time))

