
# @title: SwapPairs
# @description: TODO交换2个链表的节点
# @author  Rhett
# @date @date 2020/9/5 15:58
from algo import ListNode


class SwapPairs:
    def swappairs(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return head
        first_node=head
        second_node=head.next
        first_node.next=self.swappairs(second_node.next)
        second_node.next=first_node
        return second_node
if __name__=='__main__':
    swap=SwapPairs()
    node:ListNode =swap.swappairs(None)
    print(node)
