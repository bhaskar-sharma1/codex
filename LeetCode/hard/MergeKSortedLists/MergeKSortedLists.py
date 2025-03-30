from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        # Define a unique index for heap elements to handle duplicate values
        index = 0
        
        # Add the head of each linked list to the heap
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, index, l))
                index += 1
        
        dummy = ListNode(0)
        current = dummy

        # Extract the smallest element and push the next node from that list into the heap
        while min_heap:
            value, _, node = heapq.heappop(min_heap)
            current.next = node
            current = node
            
            if node.next:
                index += 1
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy.next


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

def test_merge_k_lists():
    sol = Solution()

    # Test Case 1: Example 1
    lists1 = [list_to_linked_list([1,4,5]), list_to_linked_list([1,3,4]), list_to_linked_list([2,6])]
    assert linked_list_to_list(sol.mergeKLists(lists1)) == [1,1,2,3,4,4,5,6]

    # Test Case 2: Empty List
    lists2 = []
    assert linked_list_to_list(sol.mergeKLists(lists2)) == []

    # Test Case 3: List with one empty list
    lists3 = [list_to_linked_list([])]
    assert linked_list_to_list(sol.mergeKLists(lists3)) == []

    # Test Case 4: Single non-empty list
    lists4 = [list_to_linked_list([1, 2, 3])]
    assert linked_list_to_list(sol.mergeKLists(lists4)) == [1, 2, 3]

    # Test Case 5: Multiple lists with duplicate values
    lists5 = [list_to_linked_list([1,1,1]), list_to_linked_list([2,2,2]), list_to_linked_list([3,3,3])]
    assert linked_list_to_list(sol.mergeKLists(lists5)) == [1,1,1,2,2,2,3,3,3]

    print("All test cases passed!")

test_merge_k_lists()
