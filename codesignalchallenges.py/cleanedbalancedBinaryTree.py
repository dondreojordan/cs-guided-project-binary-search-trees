def height(root):
    # using max bulit in function we can find height
    # first look for base case
    if root is None:
        return 0  # There is no height without a root node
    else:
        # use a recursive with max
        return max(height(root.left),height(root.right))+1

        
def balancedBinaryTree(root):
    # Check for None Nodes
    if root is None:
        return True
    # find left and right sub height
    leftheight=height(root.left)
    rightheight=height(root.right)
    # values for (leftheight - rightheight) can be 1, -1, 0 
    if (abs(leftheight - rightheight)<=1) and balancedBinaryTree( 
    root.left):
        return True
    else:
        return False