from main import *
import matplotlib.pyplot as plt
import timeit
import time
import random

select_sort = '''\
def select_sort(A: [int], k: int) -> int:
    x = A.sort()
    return (x[k])
    '''

select = '''\
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickselect(arr, k, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low == high:
        return arr[low]
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, k, low, pivot_index - 1)
    else:
        return quickselect(arr, k, pivot_index + 1, high)

def select(A, k):
    n = len(A)
    return quickselect(A, n-k)
'''


def plot(start, end, jump=1):
    x = range(start, end, jump)
    y_select = []
    y_select_sort = []
    x = []

    for n in range(start, end, jump):
        A = [random.randrange(10**3)
             for _ in range(random.randint(100, n))]
        random.shuffle(A)
        k = random.randrange(1, len(A) + 1)

        # start_time = time.process_time()
        # select(A, k)
        # end_time = time.process_time()
        # y_select.append((end_time-start_time)*10**3)

        # start_time = time.process_time()
        # select_sort(A, k)
        # end_time = time.process_time()
        # y_select_sort.append((end_time-start_time)*10**3)
        y_select_sort.append(timeit.timeit(
            select_sort, number=n, globals=globals()))
        y_select.append(timeit.timeit(select, number=n, globals=globals()))
        x.append(n)
    # print(f"y_mergeSort: {y_mergeSort}\nlength of x: {len(x)}")

    # x = 1000000
    print(y_select)
    print(y_select_sort)
    plt.plot(x, y_select, label="select (built-in)")
    plt.plot(x, y_select_sort, label="select_sort (das Gupta)")


if __name__ == "__main__":
    # plt.xscale("symlog")
    # plt.yscale("symlog")
    # plot(1, 20002, 100)
    plot(100, 1500, 10**2)
    # plot(1000, 500001, 1000)
    plt.title("Comparison between Selection Algorithms")
    plt.ylabel('Time taken (ms)')
    plt.xlabel('size of input list, $A$')
    plt.legend()
    plt.show()
