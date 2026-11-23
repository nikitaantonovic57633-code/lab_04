from time import perf_counter
import csv

from algo_lab.generators import random_list, sorted_list, reversed_list, nearly_sorted_list, duplicate_list
from algo_lab.sorting import bubble_sort, merge_sort


def measure_once(func, values):
    copy = values.copy()
    start = perf_counter()
    func(copy)
    end = perf_counter()
    return end - start


def measure_repeats(func, values):
    result = []
    for i in range(5):
        result.append(measure_once(func, values))
    return result


def main():
    with open("benchmark.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["size", "dataset", "algorithm",
                         "run_1_s", "run_2_s", "run_3_s", "run_4_s", "run_5_s"])
        for size in (100, 1000, 10000):
            datasets = (
                ("random", random_list(size, seed=52)),
                ("sorted", sorted_list(size)),
                ("reversed", reversed_list(size)),
                ("nearly_sorted", nearly_sorted_list(size, seed=52)),
                ("duplicates", duplicate_list(size, seed=52))
            )
            for name, lst in datasets:
                times = measure_repeats(bubble_sort, lst)
                writer.writerow([size, name, "bubble_sort", *times])
                times = measure_repeats(merge_sort, lst)
                writer.writerow([size, name, "merge_sort", *times])
main()