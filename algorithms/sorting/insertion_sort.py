import random

def insertion_sort(values: list[int]) -> tuple[list[int], int]:
    swap_count = 0
    
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        while j >= 0 and key < values[j]:
            values[j+1] = values[j]
            swap_count += 1
            j -= 1
        values[j+1] = key
    
    return values, swap_count

unsorted_integers = [random.randint(1, 100) for _ in range(10)]
print(f"Unsorted array: {unsorted_integers} | Number of elements: {len(unsorted_integers)}")

sorted_integers, swap_count = insertion_sort(unsorted_integers)
print(f"Sorted array: {sorted_integers} | Number of swaps performed: {swap_count}")
