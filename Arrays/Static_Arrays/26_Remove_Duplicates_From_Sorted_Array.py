from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1

        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1

        return L

if __name__ == "__main__":
    solution = Solution()
    
    nums1 = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"Original array: {nums1}")
    k1 = solution.removeDuplicates(nums1)
    print(f"Number of unique elements: {k1}")
    print(f"Modified array: {nums1[:k1]}")
    print()

    nums2 = [1, 2, 3, 4, 5]
    print(f"Original array: {nums2}")
    k2 = solution.removeDuplicates(nums2)
    print(f"Number of unique elements: {k2}")
    print(f"Modified array: {nums2[:k2]}")
    print()
    
    nums3 = [1, 1, 1, 1, 1]
    print(f"Original array: {nums3}")
    k3 = solution.removeDuplicates(nums3)
    print(f"Number of unique elements: {k3}")
    print(f"Modified array: {nums3[:k3]}")