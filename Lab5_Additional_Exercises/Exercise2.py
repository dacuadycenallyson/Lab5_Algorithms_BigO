# --- STUDENT CONFIGURATION & EXERCISE 2 ---
LAST_NAME = "Dacua"
STUDENT_ID = "TUPM-26-3491"
FAVORITE_ARTIST = "mypm"

SEED_DIGIT = int(STUDENT_ID[-1])  # 1
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 25
NAME_LENGTH = len(LAST_NAME)  # 5
ARTIST_LENGTH = len(FAVORITE_ARTIST)  # 4

# 1. Generate the two sorted enrollment datasets
# Dataset A: Ascending values using SEED_DIGIT and ID_SUM
dataset_a = [i * (SEED_DIGIT + 2) for i in range(1, ID_SUM + 1)]

# Dataset B: Ascending values using ARTIST_LENGTH and NAME_LENGTH
dataset_b = [i * ARTIST_LENGTH for i in range(1, NAME_LENGTH + 1)]

# 2. Consolidate them into one ordered collection (Merge procedure)
def merge_sorted_lists(arr1, arr2):
    i, j = 0, 0
    merged = []
    comparisons = 0
    
    while i < len(arr1) and j < len(arr2):
        comparisons += 1
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
        
    return merged, comparisons

consolidated_dataset, comp_count = merge_sorted_lists(dataset_a, dataset_b)

# 4. Verify the final order and number of records
is_sorted = all(consolidated_dataset[k] <= consolidated_dataset[k+1] for k in range(len(consolidated_dataset) - 1))
total_records_before = len(dataset_a) + len(dataset_b)
total_records_after = len(consolidated_dataset)

# 5. Time and space complexity
time_complexity = "O(N + M)"
space_complexity = "O(N + M)"

# Assessment Data Output
print("--- UNIVERSITY ENROLLMENT RECORDS (EXERCISE 2) ---")
print("Department A Dataset:", dataset_a)
print("Department B Dataset:", dataset_b)
print("Consolidated Dataset:", consolidated_dataset)
print(f"Number of records before consolidation: {total_records_before}")
print(f"Number of records after consolidation: {total_records_after}")
print(f"Comparison count: {comp_count}")
print(f"Ordering verification (Is sorted?): {is_sorted}")
print(f"Time Complexity: {time_complexity}")
print(f"Space Complexity: {space_complexity}")