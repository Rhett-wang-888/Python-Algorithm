##
# @ description: TODO 二叉树转换成链表 递归
# @ author Rhett.wang
# @ date 2020 / 8 / 2 08: 42
#
from typing import List

from algo.ListNode import TreeNode


class BinaryToTreeNode:
    def flatt(self,root:TreeNode):
        preorderList=list()
        def preorderTraversal(root:TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        preorderTraversal(root)
        size=len(preorderList)
        for i in range(1,size):
            prev,curr=preorderList[i-1],preorderList[i]
            prev.left=None
            prev.right=curr
