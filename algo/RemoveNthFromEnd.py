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
def removeNthFromEnd1(head:ListNode,n:int)->ListNode:
    def getLength(head:ListNode)->int:
        length=0
        while head:
            length+=1
            head=head.next
        return length

    dummy=ListNode(0,head)
    length=getLength(head)
    cur=dummy

    for i in range(1,length-n+1):
        cur=cur.next
    cur.next=cur.next.next

    return dummy.next

def removeNthFormEnd2(head:ListNode,n:int)->ListNode:
    dummy=ListNode(0,head)
    stack=list()
    cur=dummy
    while cur:
        stack.append(cur)
        cur=cur.next
    for i in range(n):
        stack.pop()

    prev=stack[-1]
    prev.next=prev.next.next

    return dummy.next
def removeNthFromEnd3(head:ListNode,n:int)->ListNode:
    dummy=ListNode(0,head)
    first=head
    second=dummy
    for i in range(n):
        first=first.next

    while first:
        first=first.next
        second=second.next
    second.next=second.next.next
    return dummy.next
