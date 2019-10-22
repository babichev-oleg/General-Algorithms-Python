#!/usr/bin/python3.6
def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2)
if __name__ == "__main__":
    print(fibonacci(2))
