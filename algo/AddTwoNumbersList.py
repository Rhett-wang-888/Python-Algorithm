# @title: AddTwoNumbersList
# @description: TODO
# @author  Rhett
# @date 2021/3/13 12:24
from algo import ListNode

def addTwoNumbers(l1:ListNode,l2:ListNode)->ListNode:
    head=curr=ListNode()
    carry=val=0
    while carry or l1 or l2:
        val=carry

        if l1:l1,val=l1.next,l1.val+val
        if l2:l2,val=l2.next,l2.val+val

        carry,val=divmod(val,10)
        curr.next=curr=ListNode(val)
    return head.next