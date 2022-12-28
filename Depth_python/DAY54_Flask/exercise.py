import time


def speed_calc_decorator(function):
    def wrap_decorator():
        first_time = time.time()
        function()
        difference = time.time() - first_time
        print(f"{function.__name__} run speed: {difference}")
    return wrap_decorator


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
