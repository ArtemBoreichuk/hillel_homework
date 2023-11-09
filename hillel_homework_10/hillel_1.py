def pair_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False


nums1 = [1, 2, 3, 4, 5]
target1 = 9
result1 = pair_sum(nums1, target1)
print(f"Для списку {nums1} та цільового числа {target1}: {result1}")

nums2 = [1, 2, 3, 4, 5]
target2 = 10
result2 = pair_sum(nums2, target2)
print(f"Для списку {nums2} та цільового числа {target2}: {result2}")
