class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        inorder = []
        node = root
        while True:
        	while node:
        		stack.append(node)
        		node = node.left
        	if not stack:
        		return inorder
        	node = stack.pop()
        	inorder.append(node.val)
        	node = node.right

if __name__ == "__main__":
	tn = [TreeNode(i) for i in range(8)]
	tn[0].left = tn[1];
	tn[0].right = tn[2];
	tn[1].left = tn[3];
	tn[1].right = tn[4];
	tn[2].left = tn[5];
	tn[2].right = tn[6];
	tn[4].left = tn[7];
	print Solution().inorderTraversal(tn[0])
