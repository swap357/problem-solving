''' 
Q1:
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
    
    
Q2:


    
'''

from BinaryTree import *
class NewTreeNode(TreeNode):
    def __init__(self):
        self.next = None

def connect(root):
    if not root:
        return
    if not root.left and not root.right:
        return
    r1 = root
    while r1:
        next_right_sibling = r1.next.left if r1.next else None
        r1.left.next = r1.right
        r1.right.next = next_right_sibling
        r1 = r1.next
    connect(root.left)

    