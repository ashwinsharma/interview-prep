import random

def binary_search(sorted_values: list[int], target: int):
    left = 0
    right = len(sorted_values) - 1
    comparison_count = 0

    while left <= right:
        middle = left + (right - left) // 2
        middle_value = sorted_values[middle]
        comparison_count += 1
        if middle_value < target:
            left = middle + 1
        elif middle_value > target:
            right = middle - 1
        else:
            return middle, comparison_count
    
    return -1, comparison_count

sorted_integers = sorted([random.randint(1, 100) for _ in range(10)])
print(sorted_integers)

for v in sorted_integers + [101]:
    index, comp_count = binary_search(sorted_integers, v)
    print(f"Found {v} at {index} after {comp_count} comparisons.")