# @title: GuiBingDiToShang
# @description: TODO 归并排序自顶向上的排序过程
# @author  Rhett
# @date 2021/10/25 10:33
from sort import ListNode


class GuiBing:
    def sortList(self,head:ListNode)->ListNode:
        def merge(head1:ListNode,head2:ListNode)->ListNode:
            dummyHead=ListNode(0)
            temp,temp1,temp2=dummyHead,head1,head2
            while temp1 and temp2:
                if temp1.Val<=temp2.Val:
                    temp.next=temp1
                    temp1=temp1.next
                else:
                    temp.next=temp2
                    temp2=temp2.next
                temp=temp.next

            if temp1:
                temp.next=temp1
            elif temp2:
                temp.next=temp2

            return dummyHead.next

        if not head:
            return head
        length=0
        node=head
        while node:
            length+=1
            node=node.next
        dummyHead=ListNode(0,head)
        subLength=0
        while subLength<length:
            prev,curr=dummyHead,dummyHead.next
            while curr:
                head1=curr
                for i in range(1,subLength):
                    if curr.next:
                        curr=curr.next
                    else:
                        break
                head2=curr.next
                curr.next=None
                curr=head2
                for i in range(1,subLength):
                    if curr and curr.next:
                        curr=curr.next
                    else:
                        break
                succ=None
                if curr:
                    succ=curr.next
                    curr.next=None
                merged=merge(head1,head2)
                prev.next=merged
                while prev.next:
                    prev=prev.next
                curr=succ
                subLength<<=1

        return dummyHead.next