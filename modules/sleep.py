#!/usr/bin/python3.6
import time
current_time =time.time()
time.sleep(100)
duration = time.time() - current_time
print('sleep was in 100 seconds',duration)
