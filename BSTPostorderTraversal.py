class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack = []
        postorder = []
        node = root
        while stack or node:
            
            if node:
                print "if node"
                print node.val
                stack.append(node)
                postorder = [node.val] + postorder
                node = node.right
            else:
                print "else"
                node2 = stack.pop()
                print node2.val
                node = node2.left

            print [i.val for i in stack]
            print postorder
            print "\n"
                
        return postorder

if __name__ == "__main__":
	tn = [TreeNode(i) for i in range(8)]
	tn[0].left = tn[1];
	tn[0].right = tn[2];
	tn[1].left = tn[3];
	tn[1].right = tn[4];
	tn[2].left = tn[5];
	tn[2].right = tn[6];
	tn[4].left = tn[7];
	print Solution().postorderTraversal(tn[0])
