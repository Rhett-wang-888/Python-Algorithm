# @title: RemoveNthFromEnd
# @description: TODO 删除链表倒数第n个节点
# @author  Rhett
# @date 2021/5/9 15:55
from algo import ListNode


def removeNthFromEnd(head:ListNode,n:int)->ListNode:
    def getLength(head:ListNode)->int:
        length=0
        while head:
            length +=1
            head=head.next
        return length

    dummy=ListNode(0,head)
    length=getLength(head)
    cut=dummy
    for i in range(1,length-n+1):
        cur=cur.next
    cur.next=cur.next.next
    return dummy.next