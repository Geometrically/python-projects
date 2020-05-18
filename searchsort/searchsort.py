import time
import random
import bisect
import sys

random.seed()


def insertion_sort(vals):
    for i in range(1, len(vals)):
        j = i
        while j > 0 and vals[j - 1] > vals[j]:
            vals[j], vals[j - 1] = vals[j - 1], vals[j]
            j -= 1


def bubble_sort(vals):
    n = len(vals)
    swapCompleted = True
    while swapCompleted:
        swapCompleted = False
        for i in range(n - 1):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                swapCompleted = True


def better_bubble_sort(vals):
    n = len(vals)
    swapCompleted = True
    while swapCompleted:
        swapCompleted = False
        for i in range(n - 1):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                swapCompleted = True
        n -= 1


def even_better_bubble_sort(vals):
    n = len(vals)
    while n > 0:
        new_n = 0
        for i in range(n - 1):
            if vals[i] > vals[i + 1]:
                vals[i], vals[i + 1] = vals[i + 1], vals[i]
                new_n = i + 1
        n = new_n


def selection_sort(vals):
    for i in range(len(vals)):
        minIndex = i
        for j in range(i + 1, len(vals)):
            if vals[j] < vals[minIndex]: minIndex = j
        if minIndex != i: vals[i], vals[minIndex] = vals[minIndex], vals[i]


def comb_sort(vals):
    gap = len(vals)
    shrink = 1.3
    doneSorting = False
    while not doneSorting:
        gap = int(gap / shrink)
        if gap > 1:
            doneSorting = False
        else:
            gap = 1
            doneSorting = True
        for i in range(len(vals) - gap - 1):
            if vals[i] > vals[i + gap]:
                vals[i], vals[i + gap] = vals[i + gap], vals[i]
                doneSorting = False


def merge_sort(vals):
    if len(vals) > 1:
        firstHalf = vals[:len(vals) // 2]
        secondHalf = vals[len(vals) // 2:]
        merge_sort(firstHalf)
        merge_sort(secondHalf)
        i = 0
        j = 0
        del vals[:]
        while i < len(firstHalf) or j < len(secondHalf):
            if i >= len(firstHalf):
                vals.append(secondHalf[j])
                j += 1
            elif j >= len(secondHalf):
                vals.append(firstHalf[i])
                i += 1
            else:
                if firstHalf[i] <= secondHalf[j]:
                    vals.append(firstHalf[i])
                    i += 1
                else:
                    vals.append(secondHalf[j])
                    j += 1


def better_merge_sort(vals):
    better_merge_sort_helper(vals, 0, len(vals) - 1)


def better_merge_sort_helper(vals, low, high):
    if high > low:
        middle = (low + high) // 2
        better_merge_sort_helper(vals, low, middle)
        better_merge_sort_helper(vals, middle + 1, high)
        i = low
        j = middle + 1
        nvals = []
        while i <= middle or j <= high:
            if i > middle:
                nvals.append(vals[j])
                j += 1
            elif j > high:
                nvals.append(vals[i])
                i += 1
            else:
                if vals[i] <= vals[j]:
                    nvals.append(vals[i])
                    i += 1
                else:
                    nvals.append(vals[j])
                    j += 1
        vals[low:high + 1] = nvals[:]


def quick_sort(vals):
    swaps = 0
    comparisons = 0
    swaps, comparisons = quick_sort_helper(vals, 0, len(vals) - 1, swaps, comparisons)
    return swaps, comparisons


def quick_sort_helper(vals, low, high, swaps, comparisons):
    if low < high:
        p, swaps, comparisons = partition(vals, low, high, swaps, comparisons)
        swaps, comparisons = quick_sort_helper(vals, low, p - 1, swaps, comparisons)
        swaps, comparisons = quick_sort_helper(vals, p + 1, high, swaps, comparisons)
    return swaps, comparisons


def better_quick_sort(vals):
    lowHighStack = []
    lowHighStack.append(0)
    lowHighStack.append(len(vals) - 1)
    while len(lowHighStack) > 0:
        high = lowHighStack.pop()
        low = lowHighStack.pop()
        p = partition(vals, low, high)
        if low < p - 1:
            lowHighStack.append(low)
            lowHighStack.append(p - 1)
        if p + 1 < high:
            lowHighStack.append(p + 1)
            lowHighStack.append(high)


def partition(vals, low, high, swaps, comparisons):
    pivot = vals[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if vals[j] < pivot:
            i += 1
            swaps += 1
            vals[i], vals[j] = vals[j], vals[i]
    comparisons += 1
    if vals[high] < vals[i + 1]:
        swaps += 1
        vals[i + 1], vals[high] = vals[high], vals[i + 1]
    return i + 1, swaps, comparisons


def heap_sort(vals):
    heapify(vals)
    for i in range(len(vals) - 1, -1, -1):
        vals[i], vals[0] = vals[0], vals[i]
        sift_down(vals, 0, i - 1)


def better_heap_sort(vals):
    better_heapify(vals)
    for i in range(len(vals) - 1, -1, -1):
        vals[i], vals[0] = vals[0], vals[i]
        sift_down(vals, 0, i - 1)


def heapify(vals):
    for i in range((len(vals) - 1) // 2, -1, -1):
        sift_down(vals, i, len(vals) - 1)


def better_heapify(vals):
    for i in range(1, len(vals)):
        sift_up(vals, 0, i)


def sift_up(vals, start, end):
    child = end
    while child > start:
        parent = child // 2
        if vals[parent] < vals[child]:
            vals[parent], vals[child] = vals[child], vals[parent]
            child = parent
        else:
            return


def sift_down(vals, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root
        if vals[swap] < vals[child]:
            swap = child
        if child + 1 <= end and vals[swap] < vals[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            vals[root], vals[swap] = vals[swap], vals[root]
            root = swap


def bin_index(vals, searchVal):
    i = bisect.bisect_left(vals, searchVal)
    if i != len(vals) and vals[i] == searchVal:
        return i
    else:
        raise ValueError


# MY CODE BELOW

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1", "ya", "sure", "y")

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)

    for i in range(10):
        print()

    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end="\r")


def binary_search(val, vals):
    done = False

    current_vals = vals

    while not done:
        half = len(current_vals) // 2 if len(current_vals) > 1 else 0

        if current_vals[half] < val:
            current_vals = current_vals[half:]
        elif current_vals[half] > val:
            current_vals = current_vals[:half]
        else:
            return val


def linear_search(target, vals):
    for i in range(len(vals)):
        if vals[i] == target:
            return i


def run_test(use_binary_search, randoms, search_randoms, use_progress_bar=False):
    start_time = time.time()
    el = len(search_randoms)

    if use_binary_search:
        merge_sort(randoms)

        for i, search_random in enumerate(search_randoms):
            binary_search(search_random, randoms)

            if use_progress_bar:
                print_progress_bar(i + 1, el, prefix='Binary Progress:', suffix='Complete', length=50)
    else:
        for i, search_random in enumerate(search_randoms):
            linear_search(search_random, randoms)

            if use_progress_bar:
                print_progress_bar(i + 1, el, prefix='Linear Progress:', suffix='Complete', length=50)

    total_time = time.time() - start_time

    return total_time


n = int(input("Welcome to Search and Sort! \nHow many numbers would you like in your randomly generated list?: "))

if input("Would you like to use a random list of floats(type f) or a random list of ints(type i)?: ") == "f":
    randoms = [random.random() for x in range(n)]
else:
    randoms = [random.randint(1, n) for x in range(n)]

current_el = int(input("How many numbers would you to search for?: "))

search_randoms = [random.choice(randoms) for x in range(current_el)]

use_progress_bar = str2bool(input("Would you like to use our fancy progress bar? This does slow down search times! (y/n): "))

t1 = run_test(False, randoms, search_randoms, use_progress_bar)
t2 = run_test(True, randoms, search_randoms, use_progress_bar)

print("Linear Search:", t1)
print("Binary Search Tree:", t2)
