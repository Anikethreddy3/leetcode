# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        c=0
        a=l1
        while(l2 or c):
            if l1:
                if l2:
                    s=l1.val+l2.val+c
                else:
                    s=l1.val+c
            elif l2:
                s=l2.val+c
            else :
                s=c
            l1.val=s%10
            c=s/10
            if l1.next:
                l1=l1.next
            elif l2:
                if l2.next or c:
                    l1.next=ListNode()
                    l1=l1.next
            elif c:
                l1.next=ListNode()
                l1=l1.next
            if l2:
                l2=l2.next
        return a
