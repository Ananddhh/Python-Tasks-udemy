def find_median_sorted_arrays(nums1, nums2):
    nums1.sort()
    nums2.sort()

    merged = sorted(nums1 + nums2)
    total_length = len(merged)

    if total_length % 2 == 0:
        median = merged[total_length // 2 - 1] 
    else:
        median = merged[total_length // 2]

    return median

nums1 = list(int, input("Enter the array1: ").split())   # [1, 2, 2, 4, 5, 6]
nums2 = list(int, input("Enter the array2: ").split())  # [3, 5, 2, 1, 3]

result = find_median_sorted_arrays(nums1, nums2)
print(f"The median is {result}")
