import time
from threading import Thread
from multiprocessing import Process

def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        res = func(*args, **kwargs)

        wrapper.total_time += time.time() - start
        return res
    
    wrapper.total_time = 0
    return wrapper

@timer
def test_threads(n: int):
    threads = [Thread(target=fibonacci, args=(n,)) for _ in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

@timer
def test_processes(n: int):
    procs = [Process(target=fibonacci, args=(n,)) for _ in range(10)]
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()

if __name__ == '__main__':
    n = 35

    test_threads(n)
    threads_time = test_threads.total_time

    test_processes(n)
    procs_time = test_processes.total_time

    results = f'Threads time is: {threads_time} sec\n'
    results += f'Processes time is: {procs_time} sec\n'
    with open('artifacts/task_4_1.txt', 'w') as file:
        file.write(results)
