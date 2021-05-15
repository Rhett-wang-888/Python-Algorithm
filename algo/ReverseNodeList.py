# @title: ReverseNodeList
# @description: TODO 链表指定位置翻转
# @author  Rhett
# @date 2021/5/15 15:12
from algo import ListNode


def reverseBetween(head:ListNode,left:int,right:int)->ListNode:
    def reverse_linked_list(head:ListNode):
        pre=None
        cur=head
        while cur:
            next=cur.next
            cur.next=pre
            pre=cur
            cur=next
    dummy_node=ListNode(-1)
    dummy_node.next=head
    pre=dummy_node

    for _ in range(left-1):
        pre=pre.next

    right_node=pre
    for _ in range(right-left+1):
        right_node=right_node.next
    left_node=pre.next
    curr=right_node.next

    pre.next=None
    right_node.next=None
    reverse_linked_list(left_node)

    pre.next=right_node
    left_node.next=curr
    return dummy_node.next

def reverseBetweent1(head:ListNode,right:int,left:int)->ListNode:
    dummy_node=ListNode(-1)
    dummy_node.next=head
    pre=dummy_node
    for _ in range(left-1):
        pre=pre.next
    cur=pre.next

    for _ in range(right-left):
        next=cur.next
        cur.next=next.next
        next.next=pre.next
        pre.next=next
    return dummy_node.next