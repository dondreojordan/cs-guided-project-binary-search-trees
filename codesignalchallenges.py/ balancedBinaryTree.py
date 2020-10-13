"""
You are given a binary tree and you need to write a function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node differ 
in height by a maximum of 1.

Example 1:
Given the following tree [5,10,25,None,None,12,3]:

    5
   / \
 10  25
    /  \
   12   3
return True.

Example 2:
Given the following tree [5,6,6,7,7,None,None,8,8]:

       5
      / \
     6   6
    / \
   7   7
  / \
 8   8
return False.
"""


# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

# function to find height of binary tree 
def height(root): 
      
    # base condition when binary tree root is empty 
    if root is None: 
        return 0
    return max(height(root.left), height(root.right)) + 1
  
# function to check if tree is height-balanced or not 
def balancedBinaryTree(root):
      
    # Base condition 
    if root is None: 
        return True
  
    # for left and right subtree height 
    lh = height(root.left) 
    print(lh)
    rh = height(root.right)
    print(rh) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) <= 1) and balancedBinaryTree( 
    root.left) is True and balancedBinaryTree( root.right) is True: 
        return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False


# FIGURE OUT A WAY TO PRINT OUT THE TRUE RESULTS
if __name__=="__main__":
    # root:{
    #     "value": 5,
    #     "left": {
    #         "value": 10,
    #         "left": null,
    #         "right": null
    #     },
    #     "right": {
    #         "value": 25,
    #         "left": {
    #             "value": 12,
    #             "left": null,
    #             "right": null
    #         },
    #         "right": {
    #             "value": 3,
    #             "left": null,
    #             "right": null
    #         }
    #     }
    # }
    root = Tree(5) 
    root.left = Tree(10) 
    root.right = Tree(25) 
    root.right.left = Tree(12) 
    root.right.right = Tree(3) 
    # root.left.left.left = Tree(8) 
    if balancedBinaryTree(root): 
        print("Tree is balanced") 
    else: 
        print("Tree is not balanced") 