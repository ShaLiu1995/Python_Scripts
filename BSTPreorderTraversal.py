class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return preorder

if __name__ == "__main__":
	tn = [TreeNode(i) for i in range(8)]
	tn[0].left = tn[1];
	tn[0].right = tn[2];
	tn[1].left = tn[3];
	tn[1].right = tn[4];
	tn[2].left = tn[5];
	tn[2].right = tn[6];
	tn[4].left = tn[7];
	print Solution().preorderTraversal(tn[0])
