# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#  check if p or q exist in left and right subtree. 
#  if both left and right are found, then the LCA is the root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root == p or root == q or root == None:
            return root
        
        left = self.lowestCommonAncestor(root.left, p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        if left: return left
        if right: return right
        
        