class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if(root == None):
            return None
        elif(root.val == val):
            return root
        elif(root.val>val):
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)