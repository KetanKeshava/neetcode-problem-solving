# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        if root:
            queue.append(root)

        res = []

        # level = 0  
        while len(queue) > 0:
            # print("level: ", level)
            print(queue[-1].val)
            res.append(queue[-1].val)

            for i in range(len(queue)):
                curr = queue.popleft()
                # print(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # level += 1

        return res
        