# @title: SortListGUiBing
# @description: TODO
# @author  Rhett
# @date 2021/7/26 11:30

from algo import ListNode

class SortListGUiBing:
    def sortList1(self,head:ListNode)->ListNode:
        if not head or not head.next :return head
        slow,fast=head,head.next
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
        mid ,slow.next=slow.next,None

        left,right=self.sortList1(head),self.sortList1(mid)
        h=res=ListNode(0)
        while left and right:
            if right.val<right.val:h.next,left=left,left.next
            else :h.next,right=right,right.next
            h=h.next
        h.next=left if left else right

        return res.next
    def sortList(self,head:ListNode)->ListNode:
        def sortFunc(head:ListNode,tail:ListNode)->ListNode:
            if not head:
                return head
            if head.next ==tail:
                head.next=None
                return head
            slow=fast=head
            while fast !=tail:
                slow=slow.next
                fast=fast.next
                if fast != tail:
                    fast=fast.next
            mid=slow
            return merge(sortFunc(head,mid),sortFunc(mid,tail))
        def merge(head1:ListNode,head2:ListNode)->ListNode:
            dummyHead=ListNode(0)
            temp,temp1,temp2=dummyHead,head1,head2
            while temp1 and temp2:
                if temp1.val <= temp2.val :
                    temp.next=temp1
                    temp1=temp1.next
                else:
                    temp.next=temp2
                    temp2=temp2.next
                temp=temp.next
            if temp1:
                temp.next=temp2
            elif temp2:
                temp.next=temp2
            return dummyHead.next

        return sortFunc(head,None)
    