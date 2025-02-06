import multiprocessing.process
import time 
import multiprocessing

def do_something(seconds):
    print(f"Sleeping for {seconds}(s)...")
    time.sleep(seconds)
    print(f"DONE sleeping...")

start = time.perf_counter()    

num_processes = 10

processes = []
for _ in range(num_processes):
    process = multiprocessing.Process(target=do_something, args=[1])
    process.start()
    processes.append(process)

for p in processes:
    p.join()

end = time.perf_counter()

print(f"Finished in {end-start}(s)")