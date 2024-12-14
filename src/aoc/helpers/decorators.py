import cProfile
from functools import wraps
from timeit import default_timer


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        end_time = default_timer()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds to execute.\n")
        return result

    return wrapper


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            result = func(*args, **kwargs)
        pr.print_stats(sort="time")
        return result

    return wrapper
