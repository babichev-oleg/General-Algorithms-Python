#!/usr/bin/python3.7
import time
start_time=time.time()
def fibonacci(n: int) -> int:
    First_Value = 0
    Second_Value = 1
    for Num in range(0, n):
        if(Num <= 1):
            Next = Num
        else:
            Next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = Next
            print(Next)

if __name__ == "__main__":
    print(fibonacci(10))
    print(fibonacci(500))
print("--- %s seconds ---" % (time.time() - start_time))

