# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumEvenGrandparent(self, root: TreeNode):
	res = 0
	res += sumOfNode(root,None,None)
	return res

def sumOfNode(currentNode, parent, grandparent):
	if not currentNode:
		return 0

	res = 0
	if (parent) and (grandparent % 2 == 0):
		res += currentNode.val
	return res + sumOfNode(currentNode.left, currentNode, parent) + sumOfNode(currentNode.right, currentNode, parent)
	