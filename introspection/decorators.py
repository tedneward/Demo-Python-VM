#!/usr/bin/env python3

# Python decorator examples

import datetime

# {{## BEGIN decorator ##}}
def restricted(func):
    def wrapper(*args, **kwargs):
        if 7 <= datetime.now().hour < 22:
            return func(*args, **kwargs)
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

@restricted
def say_whee():
    print("Whee!") # Only between 7 and 10!
# {{## END decorator ##}}

# {{## BEGIN timer-decorator ##}}
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
# {{## END timer-decorator ##}}
