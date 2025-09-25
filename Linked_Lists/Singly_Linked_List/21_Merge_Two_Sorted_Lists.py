from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values) if values else "Empty list"

def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

if __name__ == "__main__":
    solution = Solution()
    
    print("Merge Two Sorted Linked Lists Tests")
    print("-" * 40)
    
    print("Test 1: Normal merge")
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 4]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    print(f"List 1: {print_linked_list(list1)}")
    print(f"List 2: {print_linked_list(list2)}")
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Merged: {print_linked_list(merged)}")
    print()
    
    print("Test 2: Different lengths")
    list1_values = [1, 3, 5, 7, 9]
    list2_values = [2, 4]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    print(f"List 1: {print_linked_list(list1)}")
    print(f"List 2: {print_linked_list(list2)}")
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Merged: {print_linked_list(merged)}")
    print()
    
    print("Test 3: One empty list")
    list1_values = []
    list2_values = [1, 2, 3]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    print(f"List 1: {print_linked_list(list1)}")
    print(f"List 2: {print_linked_list(list2)}")
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Merged: {print_linked_list(merged)}")
    print()
    
    print("Test 4: Both empty lists")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    print(f"List 1: {print_linked_list(list1)}")
    print(f"List 2: {print_linked_list(list2)}")
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Merged: {print_linked_list(merged)}")
    print()
    
    print("Test 5: All elements in list1 are smaller")
    list1_values = [1, 2, 3]
    list2_values = [4, 5, 6]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    print(f"List 1: {print_linked_list(list1)}")
    print(f"List 2: {print_linked_list(list2)}")
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Merged: {print_linked_list(merged)}")
    print()
    
    print("Test 6: Lists with duplicate values")
    list1_values = [1, 1, 2, 3]
    list2_values = [1, 2, 2, 4]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    print(f"List 1: {print_linked_list(list1)}")
    print(f"List 2: {print_linked_list(list2)}")
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Merged: {print_linked_list(merged)}")
    print()
    
    print("Test 7: Verify sorted order")
    list1_values = [2, 5, 8]
    list2_values = [1, 3, 4, 6, 7, 9]
    list1 = create_linked_list(list1_values)
    list2 = create_linked_list(list2_values)
    print(f"List 1: {list1_values}")
    print(f"List 2: {list2_values}")
    merged = solution.mergeTwoLists(list1, list2)
    merged_values = linked_list_to_list(merged)
    print(f"Merged: {merged_values}")
    is_sorted = all(merged_values[i] <= merged_values[i+1] for i in range(len(merged_values)-1))
    print(f"Is sorted? {is_sorted}")