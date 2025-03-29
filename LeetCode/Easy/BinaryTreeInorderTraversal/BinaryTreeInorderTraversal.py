from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 1. Recursion Approach
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        
        result = []
        inorder(root)
        return result
    # 2. Iterative Approacch
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []
    #     stack = []
    #     current = root

    #     while current or stack:
    #         while current:
    #             stack.append(current)
    #             current = current.left  # Move to the left subtree
            
    #         current = stack.pop()  # Visit the node
    #         result.append(current.val)
            
    #         current = current.right  # Move to the right subtree
        
    #     return result

def test_inorder_traversal():
    sol = Solution()

    # Test Case 1: Example 1 -> root = [1,null,2,3]
    root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.inorderTraversal(root1) == [1, 3, 2]

    # Test Case 2: Example 2 -> root = [1,2,3,4,5,null,8,null,null,6,7,9]
    root2 = TreeNode(1,
                     TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
                     TreeNode(3, None, TreeNode(8, TreeNode(9))))
    assert sol.inorderTraversal(root2) == [4, 2, 6, 5, 7, 1, 3, 9, 8]

    # Test Case 3: Empty Tree
    assert sol.inorderTraversal(None) == []

    # Test Case 4: Single Node
    root4 = TreeNode(1)
    assert sol.inorderTraversal(root4) == [1]

    # Test Case 5: Only Left Subtree
    root5 = TreeNode(3, TreeNode(2, TreeNode(1)))
    assert sol.inorderTraversal(root5) == [1, 2, 3]

    # Test Case 6: Only Right Subtree
    root6 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert sol.inorderTraversal(root6) == [1, 2, 3]

    print("All test cases passed!")

test_inorder_traversal()
