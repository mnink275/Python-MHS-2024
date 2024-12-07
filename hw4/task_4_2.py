import time
import math

from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Process

import matplotlib.pyplot as plt

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        res = func(*args, **kwargs)

        wrapper.total_time = time.time() - start
        return res

    wrapper.total_time = 0
    return wrapper

@timer
def n_integrate(f, a, b, n_jobs, n_iter=100000000, use_procs=False):
    pool_name = 'Process' if use_procs else 'Thread'
    print(f'\nBehcnmark: n_integrate_{pool_name}_{n_jobs} started')
    if use_procs:
        pool = ProcessPoolExecutor(max_workers=n_jobs)
    else:
        pool = ThreadPoolExecutor(max_workers=n_jobs)

    step = (b - a) / n_iter
    interval = n_iter // n_jobs

    wait_list = []
    for i in range(n_jobs):
        start = a + i * interval * step
        end = start + interval * step

        future = pool.submit(integrate, f, start, end, n_iter=interval, pool_name=pool_name)
        wait_list.append(future)
        future.add_done_callback(lambda _: print(f'Integrate_{pool_name}_[{a}, {b}] done'))

    for future in wait_list:
        future.result()

def integrate(f, a, b, *, n_iter, pool_name):
    print(f'Integrate_{pool_name}_[{a}, {b}] started')

    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc

def test_integrate(use_procs):
    timings = []
    for n_jobs in range(1, 17):
        n_integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, use_procs=use_procs)
        timings.append(n_integrate.total_time)

    return timings

if __name__ == '__main__':
    thread_timings = test_integrate(use_procs=False)
    proc_timings = test_integrate(use_procs=True)

    n_jobs = [i for i in range(1, 17)]
    plt.plot(n_jobs, thread_timings, 'r.-', label='Threads')
    plt.plot(n_jobs, proc_timings,  'b.-', label='Processes')

    plt.xlabel('Number of jobs')
    plt.ylabel('Time, sec')
    plt.grid(True)
    plt.legend()
    plt.savefig('artifacts/task_4_2.png')

    plt.show()
