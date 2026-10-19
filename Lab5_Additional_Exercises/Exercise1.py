# --- STUDENT CONFIGURATION & EXERCISE 1 ---
LAST_NAME = "Dacua"
STUDENT_ID = "TUPM-26-3491"
FAVORITE_ARTIST = "mypm"

SEED_DIGIT = int(STUDENT_ID[-1])  # 1
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())  # 25
NAME_LENGTH = len(LAST_NAME)  # 5
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(ord(c.lower()) - ord('a') + 1 for c in FAVORITE_ARTIST if c.isalpha())

# 1. Generate Original Dataset (Sorted unique values)
original_dataset = [i * 3 for i in range(1, ID_SUM + 1)]

# 2. Rotate the Dataset
rotation_index = SEED_DIGIT % len(original_dataset)
rotated_dataset = original_dataset[rotation_index:] + original_dataset[:rotation_index]

# 3. Target Incident
target_incident = ID_SUM + ARTIST_SUM

print("Original Dataset:", original_dataset)
print("Rotated Dataset:", rotated_dataset)
print("Target Incident:", target_incident)

# 4. Modified Binary Search for Rotated Sorted Array
def binary_search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1, comparisons

# 5. Linear Search
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

rot_index, rot_comps = binary_search_rotated(rotated_dataset, target_incident)
lin_index, lin_comps = linear_search(rotated_dataset, target_incident)

print("\n--- RESULTS ---")
print(f"Rotated Binary Search: Index {rot_index}, Comparisons: {rot_comps}")
print(f"Linear Search: Index {lin_index}, Comparisons: {lin_comps}")