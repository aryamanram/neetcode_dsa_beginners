from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

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
    return " -> ".join(values)

def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# Test the code
if __name__ == "__main__":
    solution = Solution()
    
    print("Linked List Reversal Tests")
    print("-" * 40)
    
    print("Test 1: Normal list")
    values1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(values1)
    print(f"Original: {print_linked_list(head1)}")
    reversed1 = solution.reverseList(head1)
    print(f"Reversed: {print_linked_list(reversed1)}")
    print()
    
    print("Test 2: Two elements")
    values2 = [1, 2]
    head2 = create_linked_list(values2)
    print(f"Original: {print_linked_list(head2)}")
    reversed2 = solution.reverseList(head2)
    print(f"Reversed: {print_linked_list(reversed2)}")
    print()
    
    print("Test 3: Single element")
    values3 = [1]
    head3 = create_linked_list(values3)
    print(f"Original: {print_linked_list(head3)}")
    reversed3 = solution.reverseList(head3)
    print(f"Reversed: {print_linked_list(reversed3)}")
    print()
    
    print("Test 4: Empty list")
    head4 = create_linked_list([])
    print(f"Original: {print_linked_list(head4)}")
    reversed4 = solution.reverseList(head4)
    print(f"Reversed: {print_linked_list(reversed4)}")
    print()
    
    print("Test 5: Larger list")
    values5 = [10, 20, 30, 40, 50, 60, 70]
    head5 = create_linked_list(values5)
    print(f"Original: {print_linked_list(head5)}")
    reversed5 = solution.reverseList(head5)
    print(f"Reversed: {print_linked_list(reversed5)}")
    print()
    
    print("Test 6: List with duplicate values")
    values6 = [1, 2, 2, 3, 3, 3]
    head6 = create_linked_list(values6)
    print(f"Original: {print_linked_list(head6)}")
    reversed6 = solution.reverseList(head6)
    print(f"Reversed: {print_linked_list(reversed6)}")
    print()
    
    print("Test 7: Verify reversal correctness")
    values7 = [1, 2, 3, 4]
    head7 = create_linked_list(values7)
    print(f"Original values: {values7}")
    reversed7 = solution.reverseList(head7)
    reversed_values = linked_list_to_list(reversed7)
    print(f"Reversed values: {reversed_values}")
    print(f"Is correctly reversed? {reversed_values == values7[::-1]}")