import concurrent.futures
import multiprocessing.process
import time 
import multiprocessing
import concurrent

def do_something(seconds):
    print(f"Sleeping for {seconds}(s)...")
    time.sleep(seconds)
    print(f"DONE sleeping...")

num_processes = 10

def run_manual_multiprocessing():    
    start = time.perf_counter()   

    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=do_something, args=[1])
        process.start()
        processes.append(process)

    for p in processes:
        p.join()

    end = time.perf_counter()

    print(f"Finished in {end-start}(s)")


def run_with_process_pool_submit():
    start = time.perf_counter()    

    with concurrent.futures.ProcessPoolExecutor() as executor:
        [executor.submit(do_something, 1) for _ in range(num_processes)]

    end = time.perf_counter()

    print(f"Finished in {end-start}(s)")

def run_with_process_pool_map():
    start = time.perf_counter()    

    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds_list = [1 for _ in range(num_processes)]
        executor.map(do_something, seconds_list) 

    end = time.perf_counter()

    print(f"Finished in {end-start}(s)")


#run_manual_multiprocessing()
run_with_process_pool_submit()
run_with_process_pool_map()