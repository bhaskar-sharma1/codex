from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes left in the list
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        # If we have k nodes, reverse them
        if count == k:
            prev, curr = None, head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # Recursively process the next batch
            head.next = self.reverseKGroup(curr, k)
            return prev  # New head after reversing k nodes
        
        # If less than k nodes remain, return head as is
        return head
def list_to_linked_list(arr):
    """Helper function to convert a list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_reverse_k_group():
    sol = Solution()

    # Test Case 1: k = 2
    lists1 = list_to_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(sol.reverseKGroup(lists1, 2)) == [2, 1, 4, 3, 5]

    # Test Case 2: k = 3
    lists2 = list_to_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(sol.reverseKGroup(lists2, 3)) == [3, 2, 1, 4, 5]

    # Test Case 3: k = 1 (No change)
    lists3 = list_to_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(sol.reverseKGroup(lists3, 1)) == [1, 2, 3, 4, 5]

    # Test Case 4: k = 5 (Entire list reversed)
    lists4 = list_to_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(sol.reverseKGroup(lists4, 5)) == [5, 4, 3, 2, 1]

    # Test Case 5: k > n (No change)
    lists5 = list_to_linked_list([1, 2, 3])
    assert linked_list_to_list(sol.reverseKGroup(lists5, 4)) == [1, 2, 3]

    print("All test cases passed!")

test_reverse_k_group()
