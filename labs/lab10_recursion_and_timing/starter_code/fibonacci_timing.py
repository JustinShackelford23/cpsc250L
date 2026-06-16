import time
import matplotlib.pyplot as plt

def fib_recursive(n):
    # TODO: write this function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    # TODO: write this function
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        t1 = 0
        t2 = 1
        for i in range(2, n+1):
            t3 = t2 + t1
            t1 = t2
            t2 = t3
        return t3


def time_function(function, n):
    # TODO: write this function - google the python time module to figure out how it works
    # TODO: start a timer, call the appropriate function, then stop the timer
    # TODO: return the elapsed time
    start_time = time.perf_counter()
    function(n)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    values = [5, 10, 20, 25, 30, 35, 40]

    print("Fibonacci Timing")
    print("----------------")
    print("n    recursive_time    iterative_time")
    recurs_time =[]
    iter_time =[]
    for n in values:
        recursive_time = time_function(fib_recursive, n)
        iterative_time = time_function(fib_iterative, n)
        recurs_time.append(recursive_time)
        iter_time.append(iterative_time)
        if iterative_time != 0:
            speed = recursive_time/iterative_time
        else:
            speed = float("inf")
        print(f"{n:<5} {recursive_time:.8f} seconds    {iterative_time:.8f} seconds     {speed:.1f}")
    plt.plot(values, recurs_time, label="recursive_time")
    plt.plot(values, iter_time, label="iterative_time")
    plt.yscale("log")
    plt.xlabel('n')
    plt.ylabel('Time (s)')
    plt.title('How long recursive and iterative time takes')
    plt.show()

    # TODO: create a plot which shows both recursive time and iterative time as a function of n
    # TODO: label the x-axis, y-axis, and provide a title
    # TODO: display a legend that will indicate which dataset is which
    # TODO: make the y-axis logarithmic

main()

#Commit 1: Add recursive Fibonacci
#Commit 2: Add iterative Fibonacci
#Commit 3: Add timing code
#Commit 4: Add output table and cleanup