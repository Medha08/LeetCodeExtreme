# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if(root == None):
            return []
        q = deque()
        
        q.append(root)
        res = []
        
        
        while(q):
            levelLen = len(q)
            for i in range(levelLen):
                quNode = q.popleft()
                if(i == levelLen-1):
                    res.append(quNode.val)
                if(quNode.left):
                    q.append(quNode.left)
                if(quNode.right):
                    q.append(quNode.right)
                
        return res