def find_median_sorted_arrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    nums1.sort()
    nums2.sort()

    merged = sorted(nums1 + nums2)
    total_length = m + n

    if total_length % 2 == 0:
        median = (merged[total_length // 2 - 1] + merged[total_length // 2]) / 2
    else:
        median = merged[total_length // 2]

    return median

nums1 = [1, 2, 2, 4, 5, 6]
nums2 = [3, 5, 2, 1, 3]

result = find_median_sorted_arrays(nums1, nums2)
print(f"The median is {result}")
