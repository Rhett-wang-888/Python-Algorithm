##
# @ description: TODO 二叉树路径总和等于给定值，路径必须要以叶子节点结束 回溯算法
# @ author Rhett.wang
# @ date 2020 / 8 / 2 08: 42
#
from typing import List

from algo.ListNode import TreeNode
class Solution:
    def pathSum(self,root:TreeNode,sum:int)->List[List[int]]:
        li=[]
        if root is None:
            return li
        def find(root,sum,path):
            sum-=root.val
            if root.left is None  and root.right is None and sum==0:
                li.append(path+[root.val])
            if root.left:
                find(root.left,sum,path+[root.val])
            if root.right:
                find(root.right,sum,path+[root.val])
        find(root,sum,[])
        return li
if __name__ == '__main__':
    root:TreeNode = TreeNode(5)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    sum=8
    so=Solution()
    res=so.pathSum(root,sum)
    print(res)

