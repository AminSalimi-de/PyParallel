import multiprocessing.pool
import numpy as np
import multiprocessing
import os

def parallel_test(value):
    msg = f"value = {value} - PID = {os.getpid()}"
    print(msg)
    return msg

array = [1, 2, 3, 4, 5, 6]

print("Sequential:")
result = list(map(parallel_test, array))

print("Parallel:")
with multiprocessing.Pool(processes=6) as pool:
    result_multi_processing = pool.map(parallel_test, array)
    