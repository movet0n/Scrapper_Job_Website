

def total_runtime(func):

    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        total_time = time.time() - start_time
        print(f"\nFunction run time: {total_time} seconds")

    return wrapper
