# create a decorator that measures the time taken by a function
class Timeit:
    def __init__(self):
        self.time_accumulator = {}

    def timeit(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            # print(f"Time taken by {func.__name__}: {elapsed_time} seconds")
            
            # Accumulate the time taken
            if func.__name__ in self.time_accumulator:
                self.time_accumulator[func.__name__] += elapsed_time
            else:
                self.time_accumulator[func.__name__] = elapsed_time
            
            return result
        return wrapper

    def get_accumulated_times(self):
        return self.time_accumulator


# Create an instance of the Timeit class
timer = Timeit()
