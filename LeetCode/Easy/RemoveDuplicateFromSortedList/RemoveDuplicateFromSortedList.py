from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate node
            else:
                current = current.next  # Move to the next unique node
        return head

# Function to convert list to linked list
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to convert linked list back to list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 1, 1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], [])
    ]

    for input_list, expected in test_cases:
        linked_list = list_to_linked_list(input_list)
        output_linked_list = solution.deleteDuplicates(linked_list)
        output_list = linked_list_to_list(output_linked_list)
        print(f"Input: {input_list} | Output: {output_list} {'✅' if output_list == expected else '❌'}")
