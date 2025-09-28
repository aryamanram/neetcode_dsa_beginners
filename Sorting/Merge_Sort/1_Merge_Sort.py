# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs, s, e):
        if e - s + 1 <= 1:
            return pairs

        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)
        self.merge(pairs, s, m, e)

        return pairs

    def merge(self, arr, s, m, e):
        L = arr[s : m + 1] #Left Half of Array
        R = arr[m + 1 : e + 1] # Right Half of Array

        lPointer = 0 # index for left array
        rPointer = 0 # index for right array
        resPointer = s # index for results array

        # Merge two sorted halfs
        while lPointer < len(L) and rPointer < len(R):
            if L[lPointer].key <= R[rPointer].key:
                arr[resPointer] = L[lPointer]
                lPointer += 1
            else:
                arr[resPointer] = R[rPointer]
                rPointer += 1
            resPointer += 1

        # Below if one of the halfs has elements remaining.
        while lPointer < len(L):
            arr[resPointer] = L[lPointer]
            lPointer += 1
            resPointer += 1
        while rPointer < len(R):
            arr[resPointer] = R[rPointer]
            rPointer += 1
            resPointer += 1

