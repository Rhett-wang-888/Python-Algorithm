# @title: GuiBing
# @description: TODO 这个脚本主要是给链表进行归并排序
# @author  Rhett
# @date 2021/10/18 11:28
from sort.ListNode import ListNode


class GuiBing:
    def sortList1(self,head:ListNode)->ListNode:
        def sortFunc(head:ListNode,tail:ListNode)->ListNode:
            if not head:
                return head
            if head.next ==tail:
                head.next=None
                return head
            slow=fast=head
            while fast != tail :
                fast=fast.next
                slow=slow.next
                if fast != tail:
                    fast=fast.next
            mid =slow
            return merge(sortFunc(head,mid),sortFunc(mid,tail))
        def merge(head1:ListNode,head2:ListNode)->ListNode:
            dummyHead =ListNode(0)
            temp,temp1,temp2=dummyHead,head1,head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
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
        return sortFunc(head,None)
    def sortList(self,head:ListNode)->ListNode:
        def sortFunc(head:ListNode,tail:ListNode)->ListNode:
            if not head:
                return head
            if head.next==tail:
                head.next=None
                return head
            slow=fast=head
            while fast!=tail:
                slow=slow.next
                fast=fast.next
                if fast !=tail:
                    fast=fast.next
            mid=slow
            return merge(sortFunc(head,mid),sortFunc(mid,tail))
        def merge(head1:ListNode,head2:ListNode)->ListNode:
            dummyHead=ListNode(0)
            temp,temp1,temp2=dummyHead,head1,head2
            while temp1 and temp2:
                if temp1.val<=temp2.val:
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
        return sortFunc(head,None)