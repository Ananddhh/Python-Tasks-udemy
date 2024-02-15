def find_median_sorted_arrays():
    return True
nums1=sorted(list(input("Enter values of first array seperated by space : ").split()))
nums2=sorted(list(input("Enter values of second array seperated by space: ").split()))
nums3=sorted(nums1+nums2)
print("The array after concatenation: ",nums3)
mid=len(nums3) // 2
nums3=[int(x) for x in nums3]
if len(nums3) %2 ==0:
        result=(nums3[mid]+nums3[mid-1])/2
else:
        result=nums3[mid]
print("median: ",result)