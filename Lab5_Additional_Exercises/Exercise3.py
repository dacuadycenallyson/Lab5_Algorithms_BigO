# --- STUDENT CONFIGURATION & EXERCISE 3 ---
import time
import random

LAST_NAME = "Dacua"
STUDENT_ID = "TUPM-26-3491"
FAVORITE_ARTIST = "mypm"

ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 25

# 1. Generate base orders using student-specific inputs
base_orders = [i * 4 for i in range(1, ID_SUM + 1)]

# Create the three input conditions from the same orders
random.seed(42)
random_orders = base_orders.copy()
random.shuffle(random_orders)

sorted_orders = sorted(base_orders)
reverse_orders = sorted(base_orders, reverse=True)

input_conditions = {
    "Sorted": sorted_orders,
    "Reverse-Ordered": reverse_orders,
    "Random": random_orders
}

# 2. Sorting Algorithms implementation with performance tracking
def bubble_sort(arr):
    data = arr.copy()
    comps, moves = 0, 0
    start_time = time.perf_counter()
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                moves += 3
                swapped = True
        if not swapped:
            break
    end_time = time.perf_counter()
    return data, comps, moves, (end_time - start_time)

def selection_sort(arr):
    data = arr.copy()
    comps, moves = 0, 0
    start_time = time.perf_counter()
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            moves += 3
    end_time = time.perf_counter()
    return data, comps, moves, (end_time - start_time)

def insertion_sort(arr):
    data = arr.copy()
    comps, moves = 0, 0
    start_time = time.perf_counter()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if data[j] > key:
                data[j + 1] = data[j]
                moves += 1
                j -= 1
            else:
                break
        if j + 1 != i:
            data[j + 1] = key
            moves += 1
    end_time = time.perf_counter()
    return data, comps, moves, (end_time - start_time)

# Execution and Output Generation
print("--- E-COMMERCE ORDER PROCESSING (EXERCISE 3) ---")
print(f"Generated Order Dataset Size: {len(base_orders)}\n")

for cond_name, dataset in input_conditions.items():
    print(f"========================================")
    print(f"INPUT CONDITION: {cond_name}")
    print(f"========================================")
    
    # Apply algorithms
    b_sorted, b_comps, b_moves, b_time = bubble_sort(dataset)
    s_sorted, s_comps, s_moves, s_time = selection_sort(dataset)
    i_sorted, i_comps, i_moves, i_time = insertion_sort(dataset)
    
    # Verify sorting
    b_verify = all(b_sorted[k] <= b_sorted[k+1] for k in range(len(b_sorted)-1))
    s_verify = all(s_sorted[k] <= s_sorted[k+1] for k in range(len(s_sorted)-1))
    i_verify = all(i_sorted[k] <= i_sorted[k+1] for k in range(len(i_sorted)-1))
    
    print(f"Bubble Sort    -> Comparisons: {b_comps}, Movements: {b_moves}, Time: {b_time:.6f}s, Verified: {b_verify}")
    print(f"Selection Sort -> Comparisons: {s_comps}, Movements: {s_moves}, Time: {s_time:.6f}s, Verified: {s_verify}")
    print(f"Insertion Sort -> Comparisons: {i_comps}, Movements: {i_moves}, Time: {i_time:.6f}s, Verified: {i_verify}\n")

print("--- BIG O & CASE ANALYSIS ---")
print("• Bubble Sort: Best-case O(N) when already sorted; Worst/Average-case O(N^2) for reverse/random.")
print("• Selection Sort: O(N^2) across all conditions since it always scans remaining elements.")
print("• Insertion Sort: Best-case O(N) when sorted; Worst/Average-case O(N^2) for reverse/random[cite: 7].")