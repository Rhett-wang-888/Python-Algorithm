# @title: BSTIterator
# @description: TODO 二叉树搜索
# @author  Rhett
# @date 2021/3/28 13:15
from algo.ListNode import TreeNode


class BSTIterator:
    def __init__(self,root:TreeNode):
        self.curr=root

    def next(self)->int:
        while self.curr.left:
            left=self.curr.left
            while left.right and left.right !=self.curr:
                left=left.right
            if left.right:
                left.right=None
                break
            else:
                left.right=self.curr
                self.curr=self.curr.left
        ans=self.curr.val
        self.curr=self.curr.right
        return ans
    def hasNext(self)->bool:
        return True if self.curr else False
