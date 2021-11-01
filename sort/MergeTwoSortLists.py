# @title: MergeTwoSortLists
# @description: TODO 排序2个有序的链表
# @author  Rhett
# @date 2021/11/1 10:14

from sort import ListNode
class soluton:
   def mergeTwoSortLists(self, l1:ListNode,l2:ListNode)->ListNode:
       if l1 is None:
           return l2
       elif l2 is None:
           return l1
       elif l1.Val<=l2.Val:
           l1.next=self.mergeTwoSortLists(l1.next,l2)
           return l1
       else:
           l2.next=self.mergeTwoSortLists(l1,l2.next)
           return l2
   def mergeTwoSortLists1(self,l1:ListNode,l2:ListNode)->ListNode:
       prehead=ListNode(-1)
       pre=prehead

       while l1 and l2:
           if l1.Val<=l2.Val:
               pre.next=l1
               l1=l1.next
           else:
               pre.next=l2
               l2=l2.next
           pre=pre.next
       pre.next=l1 if l1 is not None else l2

       return prehead.next