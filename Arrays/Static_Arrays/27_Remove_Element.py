from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = 0

        for R in range(len(nums)):
            if nums[R] != val:
                nums[L] = nums[R]
                L += 1

        return L

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [3, 2, 2, 3, 4, 3, 5]
    val1 = 3
    print(f"Original array: {nums1}")
    print(f"Value to remove: {val1}")
    k1 = solution.removeElement(nums1, val1)
    print(f"Number of elements after removal: {k1}")
    print(f"Modified array (first {k1} elements): {nums1[:k1]}")
    print()
    
    nums2 = [1, 2, 4, 5]
    val2 = 3
    print(f"Original array: {nums2}")
    print(f"Value to remove: {val2}")
    k2 = solution.removeElement(nums2, val2)
    print(f"Number of elements after removal: {k2}")
    print(f"Modified array (first {k2} elements): {nums2[:k2]}")
    print()
    
    nums3 = [2, 2, 2, 2]
    val3 = 2
    print(f"Original array: {nums3}")
    print(f"Value to remove: {val3}")
    k3 = solution.removeElement(nums3, val3)
    print(f"Number of elements after removal: {k3}")
    print(f"Modified array (first {k3} elements): {nums3[:k3]}")
    print()