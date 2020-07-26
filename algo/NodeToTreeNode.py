##
# @ description: TODO 链表转换二叉搜索树高度平衡树
# @ author Rhett.wang
# @ date 2020 / 7 / 26 21: 04
#
from test.ListNode import TreeNode


class NodeToTreeNode:
    def mapListToValues(self,head):
        vals=[]
        while head:
            vals.append(head.val)
            head=head.next
        return vals

    def sortedListToBST(self,head):
        values=self.mapListToValues(head)
        def convertListToBST(l,r):
            if l >r:
                return None
            mid =(1+r)//2
            node=TreeNode(values[mid])
            if l==r:
                return node
            node.left=convertListToBST(l,mid-1)
            node.right=convertListToBST(mid+1,r)
            return node
        return convertListToBST(0, len(values) - 1)
