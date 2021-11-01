# @title: ListNode
# @description: TODO
# @author  Rhett
# @date 2021/10/18 11:28

class ListNode:
    def __init__(self,x):
        self.Val=x
        self.next=None

    def __init__(self,x,ListNode):
        self.Val=x
        self.next=ListNode
class TreeNode:
    def __init__(self,x):
        self.Val=x
        self.left=None
        self.right=None