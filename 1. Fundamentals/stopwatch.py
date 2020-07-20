import math
import time

class Stopwatch:
    def __init__(self):
        self.start = time.time() # start time
    
    def elapsed_time(self):
        # divide by 1000 to convert from ms to s
        return (time.time() - self.start) # current time minus start time gives elapsed time

# running a loop to see how long it takes to get factorial loops
def factorial_run_time_function(n):
    if n == 0:
        return 1
    else:
        for i in range(0,n):
            factorial_run_time_function(i)

if __name__ == "__main__":
    # time how long it takes to compute the sum of
    # the sqrt of all numbers from 0 to 2^16
    stopwatch1 = Stopwatch()
    LARGE_NUMBER = 2 ** 16
    sqrt_sum = 0
    for i in range(0, LARGE_NUMBER):
        sqrt_sum += math.sqrt(i)
    
    # runs almost instantly
    print(stopwatch1.elapsed_time(), sqrt_sum)

    stopwatch2 = Stopwatch()
    factorial_run_time_function(20)
    print("Factorial function takes very long: ", stopwatch2.elapsed_time())