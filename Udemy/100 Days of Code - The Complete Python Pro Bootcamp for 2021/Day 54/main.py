import time


def speed_calc_decorator(fun):
    def fun_wrapper():
        current_time = time.time()
        fun()
        print(time.time() - current_time)
    return fun_wrapper


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